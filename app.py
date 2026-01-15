#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="BFSI Customer 360 & Cross-Sell Dashboard",
    layout="wide"
)

st.title("🏦 Customer 360 Segmentation & Cross-Sell Dashboard (BFSI)")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("C:/Users/pktal/Customer 360 Segmentation/customer_360_final_with_strategy.csv")

df = load_data()

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.header("Filters")

segment_filter = st.sidebar.multiselect(
    "Select Segment",
    options=sorted(df["segment_name"].unique()),
    default=list(df["segment_name"].unique())
)

df_filt = df[df["segment_name"].isin(segment_filter)]

# -------------------------------------------------
# KPI METRICS
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df_filt))
col2.metric("Avg Income (₹)", int(df_filt["income"].mean()))
col3.metric("Avg Balance (₹)", int(df_filt["avg_balance"].mean()))
col4.metric("Avg Products per Customer", round(df_filt["product_count"].mean(), 2))

# -------------------------------------------------
# SEGMENT DISTRIBUTION
# -------------------------------------------------
st.subheader("Customer Segment Distribution")

fig1 = px.pie(
    df_filt,
    names="segment_name",
    hole=0.4
)
fig1.update_traces(textinfo="percent")
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# PRODUCT PENETRATION BY SEGMENT
# -------------------------------------------------
st.subheader("Product Penetration by Segment (Portfolio Level)")

prod_cols = ["has_credit_card", "has_loan", "has_investments"]

grp = df_filt.groupby("segment_name")

penetration = (grp[prod_cols].sum().div(grp.size(), axis=0)) * 100

penetration = penetration.sort_index()

plot_df = penetration.reset_index().melt(
    id_vars="segment_name",
    var_name="Product",
    value_name="Penetration %"
)

plot_df["Product"] = plot_df["Product"].map({
    "has_credit_card": "Credit Card",
    "has_loan": "Loan",
    "has_investments": "Investments"
})

st.vega_lite_chart(
    plot_df,
    {
        "mark": {"type": "bar", "tooltip": True},
        "encoding": {
            "x": {
                "field": "segment_name",
                "type": "nominal",
                "title": "Customer Segment",
                "axis": {"labelAngle": 0}
            },
            "y": {
                "field": "Penetration %",
                "type": "quantitative",
                "title": "Penetration (%)",
                "scale": {"domain": [0, 100]}
            },
            "color": {
                "field": "Product",
                "type": "nominal",
                "legend": {"title": "Product"}
            },
            "xOffset": {"field": "Product"}
        },
    },
    use_container_width=True
)


# -------------------------------------------------
# CROSS-SELL OFFER DISTRIBUTION
# -------------------------------------------------
st.subheader("Recommended Cross-Sell Campaign Mix")

offer_dist = (
    df_filt["cross_sell_offer"]
    .value_counts()
    .reset_index()
)

offer_dist.columns = ["Offer", "Customers"]

offer_dist = offer_dist.sort_values("Customers", ascending=False)

# st.dataframe(offer_dist)

st.vega_lite_chart(
    offer_dist,
    {
        "mark": {"type": "bar", "tooltip": True},
        "encoding": {
            "x": {
                "field": "Offer",
                "type": "nominal",
                "sort": "-y",
                "title": "Recommended Offer",
                "axis": {"labelAngle": -15}
            },
            "y": {
                "field": "Customers",
                "type": "quantitative",
                "title": "Number of Customers"
            }
        }
    },
    use_container_width=True
)


# -------------------------------------------------
# CUSTOMER 360 LOOKUP
# -------------------------------------------------
st.subheader("Customer 360 Lookup")

cust_id = st.number_input(
    "Enter Customer ID",
    min_value=int(df["customer_id"].min()),
    max_value=int(df["customer_id"].max()),
    step=1
)

cust_row = df[df["customer_id"] == cust_id]

if not cust_row.empty:
    st.markdown("### Customer Profile")

    st.dataframe(cust_row[[
        "customer_id","age","income","avg_balance",
        "segment_name","product_count","risk_score"
    ]])

    st.markdown("### Product Holdings")
    st.dataframe(cust_row[[
        "has_credit_card","has_loan","has_investments"
    ]])

    st.success(f"🎯 Recommended Offer: {cust_row['cross_sell_offer'].values[0]}")
else:
    st.warning("Customer not found.")

# -------------------------------------------------
# DOWNLOAD SEGMENTED DATA
# -------------------------------------------------
st.subheader("Download Segmented Customer Data")

csv = df_filt.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download CSV",
    csv,
    "customer_360_segmented.csv",
    "text/csv"
)





