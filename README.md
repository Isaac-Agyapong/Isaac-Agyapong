# Isaac Agyapong

Data Scientist | Health Informatics | Machine Learning & Healthcare Analytics

I have more than five years of experience working with clinical data, including managing electronic health records for more than 500,000 patients. I use data analysis and machine learning to help healthcare teams make better decisions.

**Open to data science and health analytics roles, available from May 2027.**

## Education

- **M.S. Data Science**, Florida Polytechnic University | Expected May 2027
- **B.Sc. Health Information Management**, College of Health, Yamfo, Ghana | 2022

## Skills

- **Machine learning:** regression, classification, clustering, decision trees, random forest, gradient boosting (XGBoost), k-nearest neighbors (KNN), support vector machines (SVM), PCA, UMAP, model evaluation, SHAP
- **Statistics & causal inference:** hypothesis testing, A/B testing, regression analysis, experimental design, difference-in-differences, causal forests (EconML)
- **Programming & data:** Python (pandas, NumPy, matplotlib, seaborn), SQL (PostgreSQL), R, Jupyter, Git, Streamlit
- **Visualization & BI:** Power BI (DAX), Excel (PivotTables, XLOOKUP, Power Query)
- **Healthcare data:** electronic health records, clinical data quality, data governance
- **Cloud:** AWS

**Contact:** [LinkedIn](https://www.linkedin.com/in/isaac-agyapong) · [isaacagyapong2030@gmail.com](mailto:isaacagyapong2030@gmail.com)

## Portfolio

Five healthcare projects. Click any picture to open the project.

### [Machine Learning Model for Medicaid Expansion Impact](https://github.com/Isaac-Agyapong/Medicaid_Expansion_Impact_Model)

**Python · Causal inference · EconML · Streamlit** · real US Census data

<a href="https://github.com/Isaac-Agyapong/Medicaid_Expansion_Impact_Model"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Medicaid_Expansion_Impact_Model/master/Image/app_overview.png" alt="Medicaid expansion impact web app" width="820"></a>

Medicaid is free or low-cost health insurance for people with low incomes. Since 2014, most states have let more low-income adults sign up for it; ten states have not. This model measures how much that decision itself helped, and predicts what would happen if the remaining states did the same.

- Medicaid expansion meant about **6 fewer uninsured people in every 100** low-income adults, and about **970,000 more adults had health insurance** in 2023 because of it.
- If the ten remaining states expanded, about **530,000 more adults** would have health insurance, almost half of them in Texas.
- The result passed four reliability checks, and the model was tested on states it had never seen. A web app lets anyone pick a county and see what the model estimates.

### [Health Insurance Coverage Gap Analysis](https://github.com/Isaac-Agyapong/Health_Insurance_Coverage_Gap_Analysis)

**PostgreSQL · SQL · Python · Power BI** · real US Census data

<a href="https://github.com/Isaac-Agyapong/Health_Insurance_Coverage_Gap_Analysis"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Health_Insurance_Coverage_Gap_Analysis/master/Image/dashboard_1_overview.png" alt="Health insurance coverage gap Power BI dashboard" width="820"></a>

A look at where low-income adults still have no health insurance, across every US county from 2008 to 2023.

- In states that expanded Medicaid, the share of low-income adults with no insurance fell from **37 to 16 out of every 100**. In states that did not, it fell from 46 to 29, so people there are now **almost twice as likely** to be uninsured.
- About **6.5 million** low-income adults still had no insurance in 2023, and half of them live in the states that did not expand. Texas has the highest share (40 out of 100).
- Built a database of 1.6 million records and a dashboard where anyone, such as a hospital, can look up its own county.

### [Early Warning Machine Learning Model for High-Risk Opioid Prescribing](https://github.com/Isaac-Agyapong/Opioid_Prescriber_Risk_Model)

**Python · XGBoost · SHAP · PostgreSQL · Streamlit** · ▶ **[Live app](https://opioid-early-warning.streamlit.app)**

<a href="https://opioid-early-warning.streamlit.app"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Opioid_Prescriber_Risk_Model/main/Image/app_screenshot.png" alt="Early warning model Streamlit app" width="820"></a>

A tool that predicts which prescribers (doctors, nurse practitioners and others) are likely to start prescribing far more opioids than others in their field within the next two years. It was built from 7.8 million public Medicare records.

- When the tool picks 1,000 prescribers for review, about **38%** of them really do become high prescribers. A simple rule of thumb gets **21%**, and picking at random gets **less than 1%**.
- It was tested on newer data it had never seen, the same way it would be used in real life.
- Every prediction comes with a plain explanation of why the prescriber was flagged. Anyone can try it in the **[live app](https://opioid-early-warning.streamlit.app)**.

### [Medicare Opioid Prescribing vs. Overdose Deaths](https://github.com/Isaac-Agyapong/Medicare_Opioid_Prescribing)

**PostgreSQL · Python · Power BI** · real CMS, CDC and Census data

<a href="https://github.com/Isaac-Agyapong/Medicare_Opioid_Prescribing"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Medicare_Opioid_Prescribing/main/Image/powerbi_page1.png" alt="Medicare opioid prescribing Power BI dashboard" width="820"></a>

A study of how opioid prescribing in Medicare changed from 2013 to 2024, compared with overdose deaths, using public data from Medicare, the CDC and the US Census.

- Opioid prescribing dropped by about **40%**, but overdose deaths **doubled**. Most deaths now involve fentanyl rather than prescription pills, and the states that prescribe the most are not the states with the most deaths.
- Nurse practitioners and physician assistants now write almost **a third** of Medicare opioid prescriptions, up from under a quarter in 2019.
- Built a database of 7.8 million records and an interactive dashboard with a US map, so anyone can explore the results by state and year.

### [Healthcare Claims Analytics](https://github.com/Isaac-Agyapong/Healthcare_Claims_Analytics)

**Python · SQL · Excel · Power BI**

<a href="https://github.com/Isaac-Agyapong/Healthcare_Claims_Analytics"><img src="https://raw.githubusercontent.com/Isaac-Agyapong/Healthcare_Claims_Analytics/main/Image/powerbi_page1.png" alt="Healthcare claims Power BI dashboard" width="820"></a>

An analysis of 50,000 health insurance claims (realistic sample data) to find out why claims get denied and how much money is lost.

- **$19.2 million** in charges were denied. Denials for missing pre-approval (prior authorization) **nearly doubled** in one year and are now the biggest cause.
- Claims from out-of-network providers were denied **about twice as often**, and three providers made far more billing errors than similar providers.
- Cleaned and analyzed the data in Python, SQL and Excel, and built an interactive Power BI dashboard for managers.
