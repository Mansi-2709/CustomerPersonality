import streamlit as st
import pandas as pd

st.markdown("""
<style>

st.set_page_config(
    page_title="Customer Personality Analysis",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# CSS Styling
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

.main-title {
text-align:center;
font-size:60px;
font-weight:700;
color:white;
}

.subtitle {
text-align:center;
font-size:22px;
color:white;
margin-bottom:40px;
}

.glass-card {
background: rgba(255,255,255,0.15);
border-radius:18px;
padding:30px;
backdrop-filter: blur(14px);
-webkit-backdrop-filter: blur(14px);
border:1px solid rgba(255,255,255,0.3);
box-shadow:0 8px 32px rgba(0,0,0,0.25);
color:white;
margin-bottom:30px;
}

.feature-card {
background: rgba(255,255,255,0.12);
border-radius:16px;
padding:25px;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.25);
text-align:center;
color:white;
transition:0.3s;
}

.feature-card:hover {
transform: translateY(-6px);
box-shadow:0 10px 40px rgba(0,0,0,0.35);
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------

st.markdown('<div class="main-title">Customer Personality Analysis</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Statistical Hypothesis Testing Dashboard for Customer Behavior Insights</div>', unsafe_allow_html=True)

st.write("")

# -------------------------
# Project Overview
# -------------------------

st.markdown("""
<div class="glass-card">

<h2>📌 Project Objective</h2>

This project analyzes **customer demographics and purchasing behavior** using **statistical hypothesis testing techniques**.

Statistical methods used:

• Z-Test  
• T-Test  
• One-Way ANOVA  
• Two-Way ANOVA  
• Chi-Square Test  

The goal is to identify **statistically significant relationships between customer attributes and spending behavior** and generate meaningful business insights.

</div>
""", unsafe_allow_html=True)

# -------------------------
# Dataset Overview
# -------------------------

st.markdown("""
<div class="glass-card">

<h2>📊 Dataset Overview</h2>

The dataset contains **customer demographic information, purchase behavior, and marketing campaign interactions**.

Key attributes include:

• Age and Income  
• Education level  
• Marital status  
• Spending across multiple product categories  
• Campaign acceptance behavior  
• Recency of purchases  

Total observations: **~2200 customers**

This dataset enables **behavioral segmentation and statistical inference analysis**.

</div>
""", unsafe_allow_html=True)

# -------------------------
# App Sections
# -------------------------

st.markdown("### 🔎 Explore the Application")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
    <h3>📂 Data Explorer</h3>
    <p>Interactively explore the dataset with filters and summary statistics.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
    <h3>🧪 Hypothesis Testing</h3>
    <p>Run statistical tests dynamically including T-Test, ANOVA, and Chi-Square.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
    <h3>📊 Visual Analytics</h3>
    <p>Analyze patterns using histograms, boxplots, bar charts, and correlation heatmaps.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------

st.markdown("""
<center style='color:white;margin-top:40px'>
Built with Streamlit • Customer Statistical Analysis Project
</center>
""", unsafe_allow_html=True)
