# Unwrapping Customer Delight: Optimizing Surprise Gift Strategies

---

### 👥 **Team Members**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| [Name]           | @[handle]     | [Contribution description]                                               |
| Ava Leung        | @Ava-Leung    | Pre-experiment data analysis, power analysis, presentations              |
| Nidhi Parvathala | @nidhiparvathala5 | Pre-experiment, MLRATE, Experiment data analysis      |
| Sandy Wu         | @sandywu198   | MLRATE implementation, experiment data analysis, power analysis          |

---

## 🎯 **Project Highlights**

- Analyzed the causal impact of surprise gifts on customer spending using Randomized Controlled Trials (RCTs)
- Implemented the Machine Learning Regression-Adjusted Treatment Effect (MLRATE) technique for treatment effect estimation
- Generated actionable insights to optimize marketing strategies and enhance customer loyalty for Estée Lauder
- Conducted comprehensive power analysis and EDA to inform experimental design and data-driven decision making

---

## 👩🏽‍💻 **Setup and Installation**

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sehr-abrar/estee-lauder-1b.git
   cd estee-lauder-1b
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Access the datasets**
   - Datasets are located in the `data/` folder:
     - `experiment_results_1b.parquet` — Experiment results data
     - `pre_experiment_data.parquet` — Pre-experiment baseline data

4. **Run the notebooks**
   ```bash
   jupyter notebook
   ```
   - Navigate to the `notebooks/` folder and open the desired notebook

---

## 🏗️ **Project Overview**

This project is part of the **Break Through Tech AI Program** in collaboration with **Estée Lauder** as our host company.

**Objective:** Evaluate the causal effect of surprise gifts on customer purchasing behavior and provide data-driven recommendations for optimizing gift strategies in marketing campaigns.

**Real-world Significance:** Understanding the true impact of promotional gifts on customer spending helps companies allocate marketing budgets more effectively, enhance customer experiences, and build long-term loyalty. This project demonstrates how causal inference techniques combined with machine learning can provide robust estimates of treatment effects beyond traditional A/B testing approaches.

---

## 📊 **Data Exploration**

### Datasets
- **experiment_results_1b.parquet**: Contains experimental data including treatment assignments, customer spending, and relevant features
- **pre_experiment_data.parquet**: Pre-experiment customer data used for baseline analysis and covariate selection

### Data Exploration Process
- Conducted comprehensive Exploratory Data Analysis (EDA) on both pre-experiment and experiment data
- Analyzed customer demographics, purchasing patterns, and treatment group distributions
- Identified key covariates and potential confounders for treatment effect estimation

### Key Insights
- [To be filled based on EDA findings]

### Notebooks
- `EDA_pre_experiment.ipynb` — Analysis of pre-experiment data
- `EDA_experiment.ipynb` — Analysis of experiment results
- `power_analysis.ipynb` — Statistical power calculations for experimental design

---

## 🧠 **Model Development**

### Approach
- **Causal Inference Framework**: Randomized Controlled Trial (RCT) design
- **Treatment Effect Estimation**: Machine Learning Regression-Adjusted Treatment Effect (MLRATE)
- **Standard ATE**: Traditional Average Treatment Effect estimation for comparison

### Methodology
- Implemented MLRATE to improve precision of treatment effect estimates by adjusting for covariates
- Compared standard ATE with ML-adjusted estimates to demonstrate efficiency gains
- Conducted power analysis to determine sample size requirements and detect meaningful effects

### Notebooks
- `estimating_standard_ATE.ipynb` — Standard treatment effect estimation
- `estimating_standard_ATE_Updated.ipynb` — Updated analysis incorporating refinements
- `power_analysis.ipynb` — Power calculations and sample size determination

---

## 📈 **Results & Key Findings**

### Performance Metrics
- [Treatment effect estimates to be filled]
- [Confidence intervals and statistical significance to be filled]
- [Comparison of standard vs. ML-adjusted estimates to be filled]

### Key Insights
- [Impact of surprise gifts on customer spending to be filled]
- [Heterogeneous treatment effects across customer segments to be filled]
- [Recommendations for gift strategy optimization to be filled]

### Visualizations
- Treatment effect plots
- Covariate balance checks
- Distribution of outcomes by treatment group
- Power analysis curves

---

## 🚀 **Next Steps**

### Potential Improvements
- Explore heterogeneous treatment effects across different customer segments (e.g., by purchase history, demographics)
- Implement additional machine learning models for treatment effect estimation (e.g., causal forests, meta-learners)
- Conduct sensitivity analyses to assess robustness of findings
- Develop a recommendation system for personalized gift strategies

### With More Resources
- Analyze longer-term effects on customer lifetime value and retention
- Incorporate additional data sources (e.g., website behavior, customer satisfaction surveys)
- Build a real-time decision system for gift allocation

---

## 📝 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📄 **References**

1. Chernozhukov, V., et al. (2018). "Double/debiased machine learning for treatment and structural parameters." The Econometrics Journal.
2. Imbens, G. W., & Rubin, D. B. (2015). "Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction."
3. Additional references from project notebooks and analysis

---

## 🙏 **Acknowledgements**

We would like to thank:
- Our Challenge Advisors for their guidance and support throughout the project
- Estée Lauder representatives for providing the business context and data
- Break Through Tech AI Program staff and TAs for their assistance
- Cornell Tech for hosting the AI Studio program
