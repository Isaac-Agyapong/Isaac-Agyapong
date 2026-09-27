# Isaac Agyapong

Data Scientist | Health Informatics | Machine Learning & Healthcare Analytics

I have over five years of experience working with clinical data to support healthcare decision-making, including managing electronic health records covering more than 500,000 patients.

My work spans data analytics, machine learning, statistical analysis, visualization, data governance, and data quality.

## Skills

- **Machine learning:** regression, classification, clustering,decision trees, random forest, gradient boosting/XGBoost, K-nearest neighbors (KNN), support vector machines (SVM) , PCA,UMAP, model evaluation
- **Statistics :** hypothesis testing, A/B testing, regression analysis, experimental design
- **Programming & data:** Python (pandas, NumPy, matplotlib, seaborn), SQL (PostgreSQL), Jupyter, Git , R
- **Visualization & BI:** Power BI (DAX), Excel
- **Healthcare data:** electronic health records, clinical data quality, data governance
- **Cloud**: AWS
- **Excel**: PivotTables, XLOOKUP, Power Query, charts, formulas


**Contact:** [LinkedIn](https://www.linkedin.com/in/isaac-agyapong) · [isaacagyapong2030@gmail.com](mailto:isaacagyapong2030@gmail.com)

## Education

- **M.S. Data Science**
- **B.Sc. Health Information Management**

## Portfolio

Healthcare data science projects, from data cleaning and SQL analysis to dashboards and machine learning.

### [Early Warning Machine Learning Model for High-Risk Opioid Prescribing](https://github.com/Isaac-Agyapong/Opioid_Prescriber_Risk_Model)

**Python · XGBoost · SHAP · PostgreSQL · Streamlit** · ▶ **[Live app](https://opioid-early-warning.streamlit.app)**

<a href="https://opioid-early-warning.streamlit.app"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Opioid_Prescriber_Risk_Model/main/Image/app_screenshot.png" alt="Early warning model Streamlit app" width="820"></a>

Predicts which Medicare prescribers will become opioid prescribing outliers within two years, trained on 7.8 million real CMS Part D records.

- A 1,000-prescriber review list built from the model is **37.7% correct (95% CI 34–40%)**, nearly double the 21% of the best simple rule and **84x** random selection, on a test year never used for training or tuning.
- Strict time-based evaluation (tuned on 2020, backtested on 2021, tested on 2022 → 2023-24), calibrated probabilities, bootstrap confidence intervals and a model card.
- **SHAP** explains every score; a deployed Streamlit app lets anyone score a prescriber profile and see why.

### [Medicare Opioid Prescribing vs. Overdose Deaths](https://github.com/Isaac-Agyapong/Medicare_Opioid_Prescribing)

**PostgreSQL · Python · Power BI** · real CMS, CDC and Census data

<a href="https://github.com/Isaac-Agyapong/Medicare_Opioid_Prescribing"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Medicare_Opioid_Prescribing/main/Image/powerbi_page1.png" alt="Medicare opioid prescribing Power BI dashboard" width="820"></a>

Analysis of 7.8 million Medicare Part D prescriber records (2019–2024) alongside 12 years of prescribing rates and CDC overdose deaths.

- Showed that opioid prescribing fell **39.5%** since 2013 while overdose deaths **doubled**, with **92%** of opioid deaths now involving fentanyl-type drugs, and that the highest-prescribing states are not the states with the most deaths.
- Found that nurse practitioners and PAs grew from **23% to 30%** of Medicare opioid prescriptions, and flagged **5,721** peer-outlier prescribers, 1 in 5 of them for six straight years.
- Built a PostgreSQL star schema (raw → core → analytics, 10 data-quality checks, window functions and statistical SQL) and a 4-page Power BI report generated from code, with a US tile map, hover tooltips and 53 DAX measures.

### [Healthcare Claims Analytics](https://github.com/Isaac-Agyapong/Healthcare_Claims_Analytics)

**Python · SQL · Excel · Power BI**

<a href="https://github.com/Isaac-Agyapong/Healthcare_Claims_Analytics"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Healthcare_Claims_Analytics/main/Image/powerbi_page1.png" alt="Healthcare claims Power BI dashboard" width="820"></a>

End-to-end analysis of 50,000 synthetic health insurance claims, modeled on real-world denial patterns, to find where claim revenue is being lost.

- Traced **$19.2M in denied charges** to their causes. Missing prior-authorization denials rose **99% year over year**.
- Found that out-of-network claims are denied **about twice as often** as in-network claims, and flagged 3 providers whose denial rates are 19–25 points above their peers.
- Built the full pipeline: data cleaning with validation checks in Python, 13 analytical SQL queries (CTEs and window functions), a formula-driven Excel dashboard, and a 3-page Power BI report with 22 DAX measures.
