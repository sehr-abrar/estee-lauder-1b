import uuid

import numpy as np
import pandas as pd

from faker import Faker


def generate_pre_exp_data(N=2000, seed=0xF8B41CFEAD411E05506D1AEBF53434A8):
    rng = np.random.default_rng(seed)

    aov = rng.lognormal(mean=np.log(90), sigma=0.4, size=N)

    days_since_last = rng.exponential(scale=15, size=N).astype(int)

    tenure = np.round(rng.lognormal(mean=np.log(30), sigma=1, size=N))

    loyalty_prob = 0.02 + (1 - np.exp(-tenure / 25)) * 0.06
    loyalty = rng.binomial(n=1, p=loyalty_prob)

    alpha = 10
    beta_aov = 35
    beta_loyalty = 5
    beta_aov_loyalty = 10
    beta_tenure = 4
    beta_dayslast = 20
    beta_dayslast_loyalty = 10

    revenue = (
        alpha
        + beta_aov * np.log1p(aov)
        + beta_loyalty * loyalty
        + beta_aov_loyalty * loyalty * np.sqrt(aov)
        + beta_tenure * np.log1p(tenure)
        + beta_dayslast * np.log1p(days_since_last)
        + beta_dayslast_loyalty * loyalty * np.log1p(days_since_last)
        + rng.normal(loc=0, scale=25, size=N)
    ) / 2

    faker = Faker(locale="en_US", use_weighting=True)

    df = pd.DataFrame(
        {
            "customer_id": [str(uuid.uuid4()) for _ in range(N)],
            "name": [faker.name() for _ in range(N)],
            "aov (t-1)": np.round(aov, 2),
            "days_since_last_purchase (t-1)": days_since_last,
            "tenure_in_days(t-1)": tenure.astype(int),
            "loyalty_membership": loyalty,
            "revenue (t)": np.round(revenue, 2),
        }
    )
    return df
