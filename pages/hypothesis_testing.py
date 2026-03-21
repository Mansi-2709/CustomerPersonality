import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

st.set_page_config(
    page_title="Hypothesis Testing",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv')

# Feature Engineering (EXACT)
df["Age"] = 2026 - df["Year_Birth"]

spend_cols = [col for col in df.columns if "Mnt" in col]
df["Total_Spend"] = df[spend_cols].sum(axis=1)

campaign_cols = [col for col in df.columns if "AcceptedCmp" in col]
df["Total_Campaign_Response"] = df[campaign_cols].sum(axis=1)

df["Income"].fillna(df["Income"].median(), inplace=True)

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg,#667eea,#764ba2,#6dd5ed);
}

.glass {
background: rgba(255,255,255,0.15);
padding: 25px;
border-radius: 16px;
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.3);
margin-bottom:20px;
color:white;
}

.card {
background: rgba(255,255,255,0.1);
padding: 20px;
border-radius: 14px;
border: 1px solid rgba(255,255,255,0.2);
color:white;
margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown("""
<div class="glass">
<h1>🧪 Hypothesis Testing Dashboard</h1>
<p>Business-driven statistical analysis on customer behavior</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 1️⃣ Z-TEST (Income vs Spending)
# =========================================================

st.markdown("## 1️⃣ Z-Test: Income vs Spending")

if st.button("Run Z-Test"):

    median_income = df["Income"].median()

    high_income = df[df["Income"] > median_income]["Total_Spend"]
    low_income = df[df["Income"] <= median_income]["Total_Spend"]

    mean1, mean2 = high_income.mean(), low_income.mean()
    std1, std2 = high_income.std(), low_income.std()
    n1, n2 = len(high_income), len(low_income)

    se = np.sqrt((std1**2 / n1) + (std2**2 / n2))

    z_stat = (mean1 - mean2) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    st.markdown(f"""
    <div class="card">
    <h4>📌 Hypothesis</h4>
    H₀: High income and low income customers spend equally<br>
    H₁: Spending differs between income groups

    <h4>📊 Result</h4>
    Z = {round(z_stat,4)} <br>
    p-value = {round(p_value,4)}

    <h4>📈 Means</h4>
    High Income: {round(mean1,2)} <br>
    Low Income: {round(mean2,2)}

    <h4>🧠 Conclusion</h4>
    {"Reject H₀ → Significant difference" if p_value < 0.05 else "Fail to reject H₀"}

    <h4>📖 Why this test?</h4>
    Z-test compares means between two large independent groups.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 2️⃣ T-TEST (Campaign vs Spending)
# =========================================================

st.markdown("## 2️⃣ T-Test: Campaign Impact")

if st.button("Run T-Test"):

    accepted = df[df["Total_Campaign_Response"] > 0]["Total_Spend"]
    not_accepted = df[df["Total_Campaign_Response"] == 0]["Total_Spend"]

    t_stat, p_value = stats.ttest_ind(accepted, not_accepted, equal_var=False)

    st.markdown(f"""
    <div class="card">
    <h4>📌 Hypothesis</h4>
    H₀: Campaign has no impact on spending<br>
    H₁: Campaign affects spending

    <h4>📊 Result</h4>
    T = {round(t_stat,4)} <br>
    p-value = {round(p_value,4)}

    <h4>📈 Means</h4>
    Accepted: {round(accepted.mean(),2)} <br>
    Not Accepted: {round(not_accepted.mean(),2)}

    <h4>🧠 Conclusion</h4>
    {"Reject H₀" if p_value < 0.05 else "Fail to reject H₀"}

    <h4>📖 Why this test?</h4>
    T-test compares means between two independent groups.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 3️⃣ ANOVA (Education vs Spending)
# =========================================================

st.markdown("## 3️⃣ ANOVA: Education vs Spending")

if st.button("Run ANOVA"):

    groups = [g["Total_Spend"].values for _, g in df.groupby("Education")]

    f_stat, p_value = stats.f_oneway(*groups)

    st.markdown(f"""
    <div class="card">
    <h4>📌 Hypothesis</h4>
    H₀: All education groups spend equally<br>
    H₁: At least one group differs

    <h4>📊 Result</h4>
    F = {round(f_stat,4)} <br>
    p-value = {round(p_value,4)}

    <h4>🧠 Conclusion</h4>
    {"Reject H₀" if p_value < 0.05 else "Fail to reject H₀"}

    <h4>📖 Why this test?</h4>
    ANOVA compares means across multiple groups.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Tukey Test
# -------------------------

if st.button("Run Tukey Test"):

    tukey = pairwise_tukeyhsd(
        endog=df["Total_Spend"],
        groups=df["Education"],
        alpha=0.05
    )

    st.markdown("""
    <div class="card">
    <h4>📊 Tukey Post-Hoc Results</h4>
    </div>
    """, unsafe_allow_html=True)

    st.text(tukey)

# =========================================================
# 4️⃣ CHI-SQUARE
# =========================================================

st.markdown("## 4️⃣ Chi-Square: Marital Status vs Campaign")

if st.button("Run Chi-Square"):

    df["Campaign_Accepted"] = np.where(
        df["Total_Campaign_Response"] > 0, "Yes", "No"
    )

    contingency = pd.crosstab(
        df["Marital_Status"],
        df["Campaign_Accepted"]
    )

    chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

    st.markdown(f"""
    <div class="card">
    <h4>📌 Hypothesis</h4>
    H₀: Variables are independent<br>
    H₁: Variables are associated

    <h4>📊 Result</h4>
    Chi² = {round(chi2,4)} <br>
    p-value = {round(p_value,4)}

    <h4>🧠 Conclusion</h4>
    {"Reject H₀" if p_value < 0.05 else "Fail to reject H₀"}

    <h4>📖 Why this test?</h4>
    Chi-square tests relationship between categorical variables.
    </div>
    """, unsafe_allow_html=True)

    st.write("### Contingency Table")
    st.dataframe(contingency)
