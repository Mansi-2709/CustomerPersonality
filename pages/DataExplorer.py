import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# Load Dataset
# --------------------------

df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv')

df["Age"] = 2026 - df["Year_Birth"]

spend_cols = [c for c in df.columns if "Mnt" in c]
df["Total_Spend"] = df[spend_cols].sum(axis=1)

df["Income"].fillna(df["Income"].median(), inplace=True)

# --------------------------
# CSS (Same Theme)
# --------------------------

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

.kpi-card {
background: rgba(255,255,255,0.12);
border-radius:16px;
padding:20px;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.25);
text-align:center;
color:white;
}

.section-title {
font-size:28px;
font-weight:600;
color:white;
margin-top:20px;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# Page Header
# --------------------------

st.markdown("""
<div class="glass-card">

<h1>📂 Data Explorer</h1>

Explore customer demographic and purchase data using filters and summary statistics.

</div>
""", unsafe_allow_html=True)

# --------------------------
# Sidebar Filters
# --------------------------

st.sidebar.header("🔎 Filter Data")

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (20,70)
)

income_range = st.sidebar.slider(
    "Income Range",
    int(df["Income"].min()),
    int(df["Income"].max()),
    (20000,100000)
)

education = st.sidebar.multiselect(
    "Education",
    df["Education"].unique(),
    default=df["Education"].unique()
)

marital = st.sidebar.multiselect(
    "Marital Status",
    df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique()
)

# --------------------------
# Apply Filters
# --------------------------

filtered_df = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Income"].between(income_range[0], income_range[1])) &
    (df["Education"].isin(education)) &
    (df["Marital_Status"].isin(marital))
]

# --------------------------
# KPI Cards
# --------------------------

st.markdown('<div class="section-title">Key Metrics</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
    <h4>Total Customers</h4>
    <h2>{len(filtered_df)}</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
    <h4>Average Income</h4>
    <h2>{round(filtered_df["Income"].mean(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
    <h4>Average Spending</h4>
    <h2>{round(filtered_df["Total_Spend"].mean(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
    <h4>Average Age</h4>
    <h2>{round(filtered_df["Age"].mean(),1)}</h2>
    </div>
    """, unsafe_allow_html=True)

# --------------------------
# Dataset Info
# --------------------------

st.markdown('<div class="section-title">Dataset Information</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

c1.metric("Rows", filtered_df.shape[0])
c2.metric("Columns", filtered_df.shape[1])
c3.metric("Missing Values", filtered_df.isna().sum().sum())

# --------------------------
# Data Table
# --------------------------

st.markdown('<div class="section-title">Filtered Dataset</div>', unsafe_allow_html=True)

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

# --------------------------
# Download Data
# --------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    "Download Filtered Data",
    csv,
    "filtered_customers.csv",
    "text/csv"
)
