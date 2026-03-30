import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --------------------------
# 🌌 GLOBAL GLASS THEME
# --------------------------
st.markdown("""
<style>

/* App background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

/* Titles */
.card-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Section spacing */
.section {
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# LOAD DATA
# --------------------------
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv')

# --------------------------
# FEATURE ENGINEERING
# --------------------------
df["Age"] = 2026 - df["Year_Birth"]

spend_cols = [col for col in df.columns if "Mnt" in col]
df["Total_Spend"] = df[spend_cols].sum(axis=1)

campaign_cols = [col for col in df.columns if "AcceptedCmp" in col]
df["Total_Campaign_Response"] = df[campaign_cols].sum(axis=1)

df["Income"].fillna(df["Income"].median(), inplace=True)

# --------------------------
# HEADER
# --------------------------
st.markdown("<h1 style='text-align:center;'>📊 Data Visualization</h1>", unsafe_allow_html=True)

# --------------------------
# 1️⃣ TOTAL SPEND vs MARITAL STATUS (YOUR GRAPH)
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">💰 Total Spend vs Marital Status</div>', unsafe_allow_html=True)

fig1 = px.histogram(
    df,
    x="Marital_Status",
    y="Total_Spend",
    color="Education",
    barmode="group"
)

fig1.update_traces(marker_line_color="white", marker_line_width=1)

fig1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig1, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 2️⃣ INCOME VS SPEND
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">📈 Income vs Spending</div>', unsafe_allow_html=True)

fig2 = px.scatter(
    df,
    x="Income",
    y="Total_Spend",
    color="NumDealsPurchases",
    size="Total_Campaign_Response",
    hover_data=["NumDealsPurchases"]
)

fig2.update_xaxes(range=[0, 100000])

fig2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig2, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 3️⃣ PRODUCT SPENDING (PIVOT)
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🛒 Spending by Education</div>', unsafe_allow_html=True)

pivot = pd.pivot_table(
    df,
    index="Education",
    values=[
        "MntWines","MntFruits","MntMeatProducts",
        "MntFishProducts","MntSweetProducts","MntGoldProds"
    ],
    aggfunc="sum"
).reset_index()

fig3 = px.bar(
    pivot,
    x="Education",
    y=[
        "MntWines","MntFruits","MntMeatProducts",
        "MntFishProducts","MntSweetProducts","MntGoldProds"
    ],
    barmode="stack"
)

fig3.update_traces(marker_line_color="white", marker_line_width=1)

fig3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig3, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 4️⃣ RECENCY DISTRIBUTION
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">⏳ Recency Distribution</div>', unsafe_allow_html=True)

fig4 = px.histogram(df, x="Recency", nbins=30)

fig4.update_traces(
    marker=dict(
        color="#5A67D8",
        line=dict(color="white", width=1)
    )
)

fig4.update_layout(
    bargap=0.25,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig4, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 5️⃣ HEATMAP
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🔥 Purchase Correlation</div>', unsafe_allow_html=True)

cols = [
    "NumDealsPurchases",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",
    "NumWebVisitsMonth"
]

corr = df[cols].corr()

fig5 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu",
    zmin=-1, zmax=1
)

fig5.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig5, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 6️⃣ CHANNEL DISTRIBUTION
# --------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🛍️ Purchase Channels</div>', unsafe_allow_html=True)

channel_df = pd.pivot_table(
    df,
    index="Total_Campaign_Response",
    values=[
        "NumDealsPurchases",
        "NumWebPurchases",
        "NumCatalogPurchases",
        "NumStorePurchases"
    ],
    aggfunc="sum"
).reset_index()

fig6 = px.bar(
    channel_df,
    y="Total_Campaign_Response",
    x=[
        "NumDealsPurchases",
        "NumWebPurchases",
        "NumCatalogPurchases",
        "NumStorePurchases"
    ],
    orientation="h"
)

fig6.update_traces(marker_line_color="white", marker_line_width=1)

fig6.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

st.plotly_chart(fig6, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
