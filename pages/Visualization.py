import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(layout="wide")

# --------------------------
# GLASS UI STYLING
# --------------------------
st.markdown("""
<style>

.section-card {
background: rgba(255,255,255,0.12);
padding: 25px;
border-radius: 18px;
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.25);
margin-bottom: 25px;
color:white;
}

.section-title {
font-size: 22px;
font-weight: 600;
margin-bottom: 15px;
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

df["Campaign_Accepted"] = df["Total_Campaign_Response"].apply(lambda x: "Yes" if x > 0 else "No")

df["Income"].fillna(df["Income"].median(), inplace=True)

# --------------------------
# HEADER
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">📊 Data Visualization Dashboard</div></div>', unsafe_allow_html=True)

# --------------------------
# FILTERS
# --------------------------
col1, col2 = st.columns(2)

with col1:
    income_range = st.slider("Income Range", int(df["Income"].min()), int(df["Income"].max()), (0, 100000))

with col2:
    education_filter = st.multiselect("Education", df["Education"].unique(), default=df["Education"].unique())

filtered_df = df[
    (df["Income"].between(income_range[0], income_range[1])) &
    (df["Education"].isin(education_filter))
]

# --------------------------
# 1️⃣ Income vs Spending
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">💰 Income vs Spending</div>', unsafe_allow_html=True)

fig1 = px.scatter(
    filtered_df,
    x="Income",
    y="Total_Spend",
    color="NumDealsPurchases",
    size="Total_Campaign_Response",
    hover_data=["NumDealsPurchases"]
)

fig1.update_xaxes(range=[0, 100000])

fig1.update_layout(
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig1, use_container_width=True)

st.caption("Insight: Higher income customers tend to spend more, validating income-spend relationship.")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 2️⃣ Campaign vs Spending
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">📣 Campaign Impact</div>', unsafe_allow_html=True)

plot_df = filtered_df.groupby("Campaign_Accepted")["Total_Spend"].mean().reset_index()

fig2 = px.bar(
    plot_df,
    x="Campaign_Accepted",
    y="Total_Spend",
    color="Campaign_Accepted",
    color_discrete_map={"Yes": "#ff4b5c", "No": "#00c2ff"}
)

fig2.update_traces(marker_line_color="black", marker_line_width=1)

fig2.update_layout(
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig2, use_container_width=True)

st.caption("Insight: Customers responding to campaigns show higher average spending.")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 3️⃣ Product Spend by Education
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">🛒 Product Spending by Education</div>', unsafe_allow_html=True)

pivot = filtered_df.groupby("Education")[[
    "MntWines","MntFruits","MntMeatProducts",
    "MntFishProducts","MntSweetProducts","MntGoldProds"
]].mean().reset_index()

pivot = pivot.melt(id_vars="Education", var_name="Product", value_name="Spend")

fig3 = px.bar(
    pivot,
    x="Education",
    y="Spend",
    color="Product",
    barmode="stack"
)

fig3.update_traces(marker_line_color="black", marker_line_width=1)

fig3.update_layout(
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 4️⃣ Recency Distribution
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">⏳ Customer Recency</div>', unsafe_allow_html=True)

bins = st.slider("Select Bins", 10, 50, 30)

fig4 = px.histogram(filtered_df, x="Recency", nbins=bins)

fig4.update_traces(
    marker=dict(line=dict(color="black", width=1))
)

fig4.update_layout(
    bargap=0.25,
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 5️⃣ Correlation Heatmap
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">🔥 Purchase Behavior Correlation</div>', unsafe_allow_html=True)

cols = [
    "NumDealsPurchases",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",
    "NumWebVisitsMonth"
]

corr = filtered_df[cols].corr()

fig5 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu",
    zmin=-1, zmax=1
)

fig5.update_layout(
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# 6️⃣ Channel Purchase Distribution
# --------------------------
st.markdown('<div class="section-card"><div class="section-title">🛍️ Purchase Channel Distribution</div>', unsafe_allow_html=True)

channel_df = filtered_df.groupby("Total_Campaign_Response")[[
    "NumDealsPurchases",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases"
]].sum().reset_index()

channel_df = channel_df.melt(
    id_vars="Total_Campaign_Response",
    var_name="Channel",
    value_name="Purchases"
)

fig6 = px.bar(
    channel_df,
    y="Total_Campaign_Response",
    x="Purchases",
    color="Channel",
    orientation="h"
)

fig6.update_traces(marker_line_color="black", marker_line_width=1)

fig6.update_layout(
    plot_bgcolor="rgba(255,255,255,0.95)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
