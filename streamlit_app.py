import streamlit as st

st.set_page_config(
    page_title="Customer Personality Statistical Analysis",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Custom CSS Theme
# ---------------------------

st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg, #1f4037, #99f2c8);
}

.title {
font-size:60px;
font-weight:700;
text-align:center;
color:white;
padding-top:20px;
}

.subtitle {
font-size:22px;
text-align:center;
color:white;
margin-bottom:40px;
}

.card {
background-color:linear-gradient(120deg,#667eea,#764ba2);
padding:25px;
border-radius:15px;
box-shadow:0px 6px 18px rgba(0,0,0,0.2);
margin-bottom:20px;
}

.card-title{
font-size:26px;
font-weight:600;
margin-bottom:10px;
}

.card-text{
font-size:18px;
color:#333333;
}

.feature-card{
background:linear-gradient(120deg,#667eea,#764ba2);
color:white;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 4px 14px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Title Section
# ---------------------------

st.markdown('<div class="title">Customer Personality Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Statistical Hypothesis Testing & Customer Behavior Insights Dashboard</div>', unsafe_allow_html=True)

st.write("")

# ---------------------------
# Project Overview Card
# ---------------------------

st.markdown("""
<div class="card">
<div class="card-title">📌 Project Objective</div>
<div class="card-text">

This project explores customer behavior patterns using **statistical hypothesis testing** and **data visualization**.

We apply inferential statistics techniques including:

• Z-Test  
• T-Test  
• Chi-Square Test  
• One-Way ANOVA  
• Two-Way ANOVA  

The goal is to identify **statistically significant relationships between demographics and purchasing behavior** to generate meaningful business insights.

</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Dataset Description Card
# ---------------------------

st.markdown("""
<div class="card">
<div class="card-title">📊 Dataset Overview</div>
<div class="card-text">

The dataset contains information about **customer demographics, purchasing patterns, and marketing campaign responses**.

Key attributes include:

• Age & Income  
• Education Level  
• Marital Status  
• Spending across product categories  
• Marketing campaign acceptance  
• Recency of purchases  

Total records: **~2200 customers**

These features allow us to conduct **behavioral segmentation and statistical inference analysis.**

</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Feature Highlights
# ---------------------------

st.markdown("### 🔎 What You Can Explore In This App")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>📂 Data Explorer</h3>
    <p>Filter and inspect customer data interactively with summary statistics.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>🧪 Hypothesis Testing</h3>
    <p>Run statistical tests like T-Test, ANOVA, and Chi-Square dynamically.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>📊 Visual Analytics</h3>
    <p>Understand patterns using interactive charts and statistical visuals.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------------------
# Footer Section
# ---------------------------

st.markdown("""
<center style='color:white;margin-top:40px'>
Built with ❤️ using Streamlit | Statistical Analysis Project
</center>
""", unsafe_allow_html=True)
