import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

st.set_page_config(
    page_title="Hypothesis Testing",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv("https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv")

df["Age"] = 2026 - df["Year_Birth"]
spend_cols = [c for c in df.columns if "Mnt" in c]
df["Total_Spend"] = df[spend_cols].sum(axis=1)
df["Income"].fillna(df["Income"].median(), inplace=True)

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg,#667eea,#764ba2,#6dd5ed);
background-size: 400% 400%;
animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
0% {background-position:0% 50%;}
50% {background-position:100% 50%;}
100% {background-position:0% 50%;}
}

.glass-card {
background: rgba(255,255,255,0.15);
border-radius:18px;
padding:25px;
backdrop-filter: blur(14px);
border:1px solid rgba(255,255,255,0.3);
box-shadow:0 8px 32px rgba(0,0,0,0.25);
color:white;
margin-bottom:25px;
}

.result-card {
background: rgba(255,255,255,0.12);
border-radius:16px;
padding:20px;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.25);
color:white;
margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown("""
<div class="glass-card">
<h1>🧪 Hypothesis Testing Dashboard</h1>
Run statistical tests to uncover significant relationships.
</div>
""", unsafe_allow_html=True)

# -------------------------
# Select Test
# -------------------------

test_type = st.selectbox(
    "Select Test",
    ["T-Test", "One-Way ANOVA", "Two-Way ANOVA", "Chi-Square"]
)

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include="object").columns.tolist()

# -------------------------
# Dynamic Inputs
# -------------------------

if test_type == "T-Test":

    col = st.selectbox("Numeric Variable", numeric_cols)
    group = st.selectbox("Grouping Variable", categorical_cols)

    categories = df[group].dropna().unique()
    cat1 = st.selectbox("Group 1", categories)
    cat2 = st.selectbox("Group 2", categories, index=1)

elif test_type == "One-Way ANOVA":

    col = st.selectbox("Numeric Variable", numeric_cols)
    group = st.selectbox("Categorical Variable", categorical_cols)

elif test_type == "Two-Way ANOVA":

    col = st.selectbox("Numeric Variable", numeric_cols)
    factor1 = st.selectbox("Factor 1", categorical_cols)
    factor2 = st.selectbox("Factor 2", categorical_cols, index=1)

elif test_type == "Chi-Square":

    var1 = st.selectbox("Variable 1", categorical_cols)
    var2 = st.selectbox("Variable 2", categorical_cols, index=1)

# -------------------------
# Run Test
# -------------------------

if st.button("Run Test"):

    alpha = 0.05

    # -------------------------
    # Hypothesis + Explanation
    # -------------------------

    if test_type == "T-Test":

        H0 = "Means of two groups are equal"
        H1 = "Means of two groups are different"
        why = "Used to compare means between two independent groups."

        g1 = df[df[group] == cat1][col]
        g2 = df[df[group] == cat2][col]

        n1, n2 = len(g1), len(g2)

        # Assumptions
        norm1 = stats.shapiro(g1)[1]
        norm2 = stats.shapiro(g2)[1]
        levene_p = stats.levene(g1, g2)[1]

        t_stat, p_val = stats.ttest_ind(g1, g2, equal_var=False)

        result = f"T = {round(t_stat,4)}, p = {round(p_val,4)}"

    elif test_type == "One-Way ANOVA":

        H0 = "All group means are equal"
        H1 = "At least one group mean differs"
        why = "Used to compare means across multiple groups."

        groups = [g[col].values for _, g in df.groupby(group)]
        sizes = [len(g) for g in groups]

        f_stat, p_val = stats.f_oneway(*groups)

        # Assumption
        levene_p = stats.levene(*groups)[1]

        result = f"F = {round(f_stat,4)}, p = {round(p_val,4)}"

    elif test_type == "Two-Way ANOVA":

        H0 = "No effect of factors and no interaction"
        H1 = "At least one factor or interaction is significant"
        why = "Tests effect of two categorical variables and their interaction."

        formula = f"{col} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})"
        model = ols(formula, data=df).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)

        result = anova_table.to_string()
        p_val = anova_table["PR(>F)"].min()

    elif test_type == "Chi-Square":

        H0 = "Variables are independent"
        H1 = "Variables are associated"
        why = "Tests relationship between categorical variables."

        contingency = pd.crosstab(df[var1], df[var2])
        chi2, p_val, _, _ = stats.chi2_contingency(contingency)

        result = f"Chi2 = {round(chi2,4)}, p = {round(p_val,4)}"

    # -------------------------
    # Interpretation
    # -------------------------

    conclusion = "Reject H₀ → Significant result" if p_val < alpha else "Fail to Reject H₀ → Not significant"

    # -------------------------
    # Display Output
    # -------------------------

    st.markdown(f"""
    <div class="result-card">

    <h3>📌 Hypothesis</h3>
    <p><b>H₀:</b> {H0}</p>
    <p><b>H₁:</b> {H1}</p>

    <h3>📊 Test Result</h3>
    <p>{result}</p>

    <h3>🧠 Interpretation</h3>
    <p>{conclusion}</p>

    <h3>📖 Why this test?</h3>
    <p>{why}</p>

    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # Assumptions Panel
    # -------------------------

    if test_type in ["T-Test", "One-Way ANOVA"]:

        st.markdown(f"""
        <div class="result-card">

        <h3>⚙️ Assumption Checks</h3>

        <p><b>Normality p-values:</b> {round(norm1,4) if test_type=='T-Test' else 'Multiple groups'}</p>
        <p><b>Equal Variance (Levene Test p-value):</b> {round(levene_p,4)}</p>

        </div>
        """, unsafe_allow_html=True)

    # -------------------------
    # Sample Size
    # -------------------------

    if test_type == "T-Test":
        st.info(f"Sample Sizes → {cat1}: {n1}, {cat2}: {n2}")

    elif test_type == "One-Way ANOVA":
        st.info(f"Group Sizes: {sizes}")
