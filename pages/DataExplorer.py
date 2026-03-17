import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Explorer", layout="wide")

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv')

df["Age"] = 2026 - df["Year_Birth"]
spend_cols = [c for c in df.columns if "Mnt" in c]
df["Total_Spend"] = df[spend_cols].sum(axis=1)

# -------------------------
# CSS Styling (Same Theme)
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

.section-title {
font-size:30px;
font-weight:600;
color:white;
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Page Title
# -------------------------

st.markdown("""
<div class="glass-card">

<h1>📂 Data Explorer</h1>

Explore customer demographic and purchasing data interactively using filters and statistical summaries.

</div>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar Filters
# -------------------------

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
    "Education Level",
    options=df["Education"].unique(),
    default=df["Education"].unique()
)

marital = st.sidebar.multiselect(
    "Marital Status",
    options=df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique()
)

# -------------------------
# Apply Filters
# -------------------------

filtered_df = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Income"].between(income_range[0], income_range[1])) &
    (df["Education"].isin(education)) &
    (df["Marital_Status"].isin(marital))
]

# -------------------------
# Summary Statistics
# -------------------------

st.markdown('<div class="section-title">📊 Summary Statistics</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(filtered_df))

with col2:
    st.metric("Average Income", round(filtered_df["Income"].mean(),2))

with col3:
    st.metric("Average Spending", round(filtered_df["Total_Spend"].mean(),2))

# -------------------------
# Data Table
# -------------------------

st.markdown('<div class="section-title">📋 Dataset Preview</div>', unsafe_allow_html=True)

st.dataframe(filtered_df, use_container_width=True)

# -------------------------
# Visualizations
# -------------------------

st.markdown('<div class="section-title">📈 Quick Visualizations</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

# Age Distribution
with c1:
    fig = px.histogram(
        filtered_df,
        x="Age",
        nbins=20,
        title="Age Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Spending Boxplot
with c2:
    fig = px.box(
        filtered_df,
        x="Education",
        y="Total_Spend",
        title="Spending by Education"
    )
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Correlation Heatmap
# -------------------------

st.markdown('<div class="section-title">🔥 Correlation Heatmap</div>', unsafe_allow_html=True)

corr = filtered_df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Feature Correlation Matrix"
)

st.plotly_chart(fig, use_container_width=True)
