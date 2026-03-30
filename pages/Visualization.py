import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Visualization",
    layout="wide"
)

# --------------------------
# 🌈 PREMIUM THEME UPGRADE
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

/* Titles */
.main-title {
text-align:center;
font-size:52px;
font-weight:700;
color:white;
margin-bottom:5px;
}

.subtitle {
text-align:center;
font-size:20px;
color:rgba(255,255,255,0.85);
margin-bottom:35px;
}

/* GRID */
.row {
display: flex;
gap: 25px;
margin-bottom: 25px;
}

.col {
flex: 1;
}

/* GLASS CARD PREMIUM */
.glass-card {
background: rgba(255,255,255,0.12);
border-radius:20px;
padding:25px;
backdrop-filter: blur(18px);
-webkit-backdrop-filter: blur(18px);
border:1px solid rgba(255,255,255,0.25);
box-shadow:0 10px 40px rgba(0,0,0,0.25);
color:white;
transition: all 0.35s ease;
}

/* Hover Effect */
.glass-card:hover {
transform: translateY(-6px) scale(1.01);
box-shadow:0 20px 60px rgba(0,0,0,0.35);
}

/* Titles inside cards */
.card-title {
font-size:20px;
font-weight:600;
margin-bottom:10px;
}

/* Insight text */
.card-desc {
font-size:14px;
color:rgba(255,255,255,0.85);
margin-bottom:15px;
line-height:1.6;
}

/* Fade animation */
.fade-in {
animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
0% {opacity:0; transform:translateY(10px);}
100% {opacity:1; transform:translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# HEADER
# --------------------------
st.markdown("""
<div class="glass-card fade-in">
<h1>📊 Data Visualization</h1>
<p>Customer Personality Analysis Dashboard</p>
</div>
""", unsafe_allow_html=True)

# --------------------------
# LOAD DATA
# --------------------------
df = pd.read_csv('https://raw.githubusercontent.com/Mansi-2709/CustomerPersonality/refs/heads/master/marketing_campaign.csv')

df["Age"] = 2026 - df["Year_Birth"]

spend_cols = [col for col in df.columns if "Mnt" in col]
df["Total_Spend"] = df[spend_cols].sum(axis=1)

campaign_cols = [col for col in df.columns if "AcceptedCmp" in col]
df["Total_Campaign_Response"] = df[campaign_cols].sum(axis=1)

df["Income"].fillna(df["Income"].median(), inplace=True)

# --------------------------
# COMMON STYLE
# --------------------------
def style_fig(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        margin=dict(l=10, r=10, t=10, b=10)
    )
    for trace in fig.data:
        if trace.type in ["bar", "histogram", "scatter"]:
            trace.marker.line.color = "white"
            trace.marker.line.width = 1
    return fig

# --------------------------
# ROW 1
# --------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card-title">💰 Total Spend vs Marital Status</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Compare spending behavior across marital groups segmented by education level.</div>', unsafe_allow_html=True)

    fig1 = px.histogram(
        df,
        x="Marital_Status",
        y="Total_Spend",
        color="Education",
        barmode="group"
    )
    st.plotly_chart(style_fig(fig1), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-title">📈 Income vs Spending</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Identify high-value customers and observe spending patterns relative to income.</div>', unsafe_allow_html=True)

    fig2 = px.scatter(
        df,
        x="Income",
        y="Total_Spend",
        color="NumDealsPurchases",
        size="Total_Campaign_Response"
    )
    fig2.update_xaxes(range=[0, 100000])

    st.plotly_chart(style_fig(fig2), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# ROW 2
# --------------------------
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card-title">🛒 Spending by Education</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Breakdown of product category spending across education levels.</div>', unsafe_allow_html=True)

    pivot = pd.pivot_table(
        df,
        index="Education",
        values=[
            "MntWines","MntFruits","MntMeatProducts",
            "MntFishProducts","MntSweetProducts","MntGoldProds"
        ],
        aggfunc="sum"
    ).reset_index()

    fig3 = px.bar(pivot, x="Education", y=pivot.columns[1:], barmode="stack")
    st.plotly_chart(style_fig(fig3), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card-title">⏳ Recency Distribution</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Understand how recently customers interacted with the business.</div>', unsafe_allow_html=True)

    fig4 = px.histogram(df, x="Recency", nbins=30)
    st.plotly_chart(style_fig(fig4), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# ROW 3
# --------------------------
col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="card-title">🔥 Purchase Correlation</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Correlation between different purchase channels.</div>', unsafe_allow_html=True)

    cols = [
        "NumDealsPurchases","NumWebPurchases",
        "NumCatalogPurchases","NumStorePurchases",
        "NumWebVisitsMonth"
    ]

    fig5 = px.imshow(df[cols].corr(), text_auto=True, color_continuous_scale="RdBu", zmin=-1, zmax=1)
    st.plotly_chart(style_fig(fig5), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="card-title">🛍️ Purchase Channels</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Channel preference based on campaign response levels.</div>', unsafe_allow_html=True)

    channel_df = pd.pivot_table(
        df,
        index="Total_Campaign_Response",
        values=[
            "NumDealsPurchases","NumWebPurchases",
            "NumCatalogPurchases","NumStorePurchases"
        ],
        aggfunc="sum"
    ).reset_index()

    fig6 = px.bar(
        channel_df,
        y="Total_Campaign_Response",
        x=channel_df.columns[1:],
        orientation="h"
    )

    st.plotly_chart(style_fig(fig6), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
