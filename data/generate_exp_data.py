# Here we simply reused the above function generate_pre_exp_data, but used a different seed (to make sure the dataset generates newer, but similar customers!). Then we:
# 1. Randomly assigned them into treatment and control groups
# 2. Applied an arbitrary effect to the treatment group using the following code:


import argparse

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class ExperimentData:
    def __init__(self, seed: int):
        self.seed = seed
        self.rng = np.random.default_rng(self.seed)

    def sample(self, df: pd.DataFrame, sample_size: int) -> pd.DataFrame:
        return df.sample(sample_size, random_state=self.rng)

    def assign(self, df: pd.DataFrame) -> pd.DataFrame:
        df["assignment"] = self.rng.binomial(n=1, p=0.5, size=df.shape[0])
        return df

    def apply_treatment(
        self,
        df: pd.DataFrame,
        effect_decay_threshold: float = 150,
        effect_decay_rate: float = 0.04,
        treatment_effect: float = 0.05,
    ):
        if "assignment" not in df.columns:
            raise ValueError(
                "Expected a column `assignment` in the dataframe."
            )

        treatment_mask = df["assignment"] == 1

        revenue_t = df.loc[treatment_mask, "revenue (t)"]

        decay = np.exp(
            -1 * effect_decay_rate * (revenue_t - effect_decay_threshold)
        )

        lift = treatment_effect * np.where(
            revenue_t >= effect_decay_threshold, decay, 1
        )
        df.loc[treatment_mask, "revenue (t)"] *= 1 + lift

        return df

    def plot_treatment_effect(
        self,
        df: pd.DataFrame,
        effect_decay_threshold: float = 150,
        artifacts_dir: Path = Path("artifacts"),
    ):
        if "assignment" not in df.columns or "revenue (t)" not in df.columns:
            raise ValueError(
                "DataFrame must contain 'assignment' and 'revenue (t)' columns."
            )

        plt.figure(figsize=(10, 6))
        sns.kdeplot(
            data=df,
            x="revenue (t)",
            hue="assignment",
            fill=True,
            common_norm=False,
        )

        plt.axvline(
            x=effect_decay_threshold,
            color="r",
            linestyle="--",
            label=f"Effect Decay Threshold ({effect_decay_threshold})",
        )

        plt.title("Distribution of Revenue by Assignment Group")
        plt.legend(title="Assignment", labels=["Treatment (1)", "Control (0)"])
        plt.savefig(artifacts_dir / "treatment_effect_distribution.png")
        plt.close()

    def plot_lift_vs_revenue(
        self,
        original_df: pd.DataFrame,
        treated_df: pd.DataFrame,
        artifacts_dir: Path = Path("artifacts"),
        effect_decay_rate: float = 0.04,
        treatment_effect: float = 0.05,
        effect_decay_threshold: float = 150,
    ):
        """
        Plots the applied lift vs. original revenue for the treatment group.
        """
        treatment_mask = original_df["assignment"] == 1

        original_revenue = original_df.loc[treatment_mask, "revenue (t)"]
        treated_revenue = treated_df.loc[treatment_mask, "revenue (t)"]

        applied_lift = (treated_revenue / original_revenue) - 1
        print(f"Mean applied lift = {100*applied_lift.mean():.2f}%")

        plt.figure(figsize=(12, 7))

        # Plot the actual applied lift
        sns.scatterplot(
            x=original_revenue,
            y=applied_lift,
            label="Applied Lift",
            alpha=0.5,
            s=10,
        )

        # Overlay the theoretical lift curve for verification
        x_vals = np.linspace(
            original_revenue.min(), original_revenue.max(), 500
        )
        decay = np.exp(
            -1 * effect_decay_rate * (x_vals - effect_decay_threshold)
        )
        theoretical_lift = treatment_effect * np.where(
            x_vals >= effect_decay_threshold, decay, 1
        )
        plt.plot(
            x_vals,
            theoretical_lift,
            color="red",
            linestyle="--",
            label="Theoretical Lift Curve",
        )

        plt.axvline(
            x=effect_decay_threshold,
            color="green",
            linestyle=":",
            label=f"Effect Decay Threshold ({effect_decay_threshold})",
        )

        plt.title("Treatment Effect (Lift) vs. Original Revenue")
        plt.xlabel("Original Revenue (t)")
        plt.ylabel("Applied Lift (%)")
        plt.legend()
        plt.grid(True, which="both", linestyle="--", linewidth=0.5)

        plt.savefig(artifacts_dir / "lift_vs_revenue.png")
        plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--N", type=int, default=2772 * 2, help="Number of data points"
    )
    parser.add_argument(
        "--seed", type=int, default=0x4E1C2A9FDB837C50A691B4D2E8F6A3C7
    )
    parser.add_argument("--effect-decay-threshold", type=float, default=150)
    parser.add_argument("--effect-decay-rate", type=int, default=0.04)
    parser.add_argument("--treatment-effect", type=int, default=0.05)

    args = parser.parse_args()

    experiment_df = pd.read_parquet("experiment_data.parquet")

    exp_data = ExperimentData(args.seed)
    sample = exp_data.sample(experiment_df, args.N)
    assigned_sample = exp_data.assign(sample)

    experiment_results = exp_data.apply_treatment(
        df=assigned_sample.copy(),
        effect_decay_threshold=args.effect_decay_threshold,
        effect_decay_rate=args.effect_decay_rate,
        treatment_effect=args.treatment_effect,
    )
    print(experiment_results.head())

    group_means = experiment_results.groupby("assignment")[
        "revenue (t)"
    ].mean()
    control_mean_revenue = group_means.get(0, 0)
    treatment_mean_revenue = group_means.get(1, 0)
    print(f"Sample size    = {experiment_results.shape[0]}")
    print(f"Control mean   = ${control_mean_revenue:.2f}")
    print(f"Treatment mean = ${treatment_mean_revenue:.2f}")
    print(
        f"Observed difference in sample means = ${treatment_mean_revenue - control_mean_revenue:.2f}"
    )

    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)

    exp_data.plot_treatment_effect(
        experiment_results,
        artifacts_dir=artifacts_dir,
        effect_decay_threshold=args.effect_decay_threshold,
    )
    exp_data.plot_lift_vs_revenue(
        original_df=assigned_sample,
        treated_df=experiment_results,
        artifacts_dir=artifacts_dir,
        effect_decay_threshold=args.effect_decay_threshold,
        effect_decay_rate=args.effect_decay_rate,
        treatment_effect=args.treatment_effect,
    )

    experiment_results.to_parquet("experiment_results.parquet")
