import streamlit as st

st.set_page_config(
    page_title="Insights",
    layout="wide"
)

# -------------------------
# CSS (Glass + Premium)
# -------------------------

st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#667eea,#764ba2,#6dd5ed);
}

.glass {
background: rgba(255,255,255,0.15);
padding: 25px;
border-radius: 18px;
backdrop-filter: blur(14px);
border: 1px solid rgba(255,255,255,0.3);
margin-bottom: 20px;
color:white;
}

.insight-card {
background: rgba(255,255,255,0.1);
padding: 20px;
border-radius: 14px;
border: 1px solid rgba(255,255,255,0.2);
color:white;
margin-bottom: 15px;
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

# -------------------------
# Header
# -------------------------

st.markdown("""
<div class="glass">
<h1>📊 Business Insights Dashboard</h1>
<p>Translating statistical analysis into actionable business strategy</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 1️⃣ Executive Summary
# =========================================================

st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

Customer behavior analysis reveals that **income, marketing campaigns, and education level significantly influence spending patterns**.  

High-income customers consistently show higher purchase behavior, while campaign-engaged users demonstrate strong responsiveness.  

This suggests opportunities for **targeted marketing, segmentation strategies, and optimized campaign allocation**.

</div>
""", unsafe_allow_html=True)

# =========================================================
# 2️⃣ Key Insights
# =========================================================

st.markdown('<div class="section-title">Key Insights</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="insight-card">

    <h4>💰 Income vs Spending</h4>
    High-income customers spend significantly more than low-income groups.

    <b>Business Meaning:</b><br>
    Premium customers contribute disproportionately to revenue.

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="insight-card">

    <h4>📢 Campaign Effectiveness</h4>
    Customers who accepted campaigns show higher spending.

    <b>Business Meaning:</b><br>
    Marketing campaigns are effective in driving revenue.

    </div>
    """, unsafe_allow_html=True)

c3, c4 = st.columns(2)

with c3:
    st.markdown("""
    <div class="insight-card">

    <h4>🎓 Education Impact</h4>
    Spending varies across education levels.

    <b>Business Meaning:</b><br>
    Different customer segments behave differently.

    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="insight-card">

    <h4>💍 Marital Status Behavior</h4>
    Campaign acceptance varies across marital groups.

    <b>Business Meaning:</b><br>
    Relationship-based targeting can improve campaign success.

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 3️⃣ Business Recommendations
# =========================================================

st.markdown('<div class="section-title">Business Recommendations</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

<h4>🎯 1. Target High-Income Customers</h4>
Focus premium campaigns and exclusive offers on high-income segments.

<h4>📢 2. Optimize Marketing Campaigns</h4>
Invest more in campaigns since they directly influence spending behavior.

<h4>🧩 3. Segment Customers by Education</h4>
Create personalized strategies for different education groups.

<h4>💡 4. Personalize Based on Marital Status</h4>
Tailor campaigns based on lifestyle differences across marital segments.

</div>
""", unsafe_allow_html=True)

# =========================================================
# 4️⃣ Final Takeaways
# =========================================================

st.markdown('<div class="section-title">Final Takeaways</div>', unsafe_allow_html=True)

st.markdown("""
<div class="glass">

✔ Customer segmentation is critical for maximizing revenue  
✔ Marketing campaigns are a strong growth driver  
✔ Data-driven targeting can significantly improve ROI  

</div>
""", unsafe_allow_html=True)
