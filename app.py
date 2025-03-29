import streamlit as st
st.set_page_config(page_title="RFM Segmentation Dashboard", page_icon="📊", layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 RFM Segmentation Dashboard")
st.markdown("Analyze customer segments based on Recency, Frequency, and Monetary value.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/rfm_scores.csv")
    return df

rfm = load_data()

# Score segmentation (simple quantile-based binning)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# Create combined segment
rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].astype(int).sum(axis=1)

# Define segment labels (simplified logic)
def assign_segment(score):
    if score >= 13:
        return "Champions"
    elif score >= 10:
        return "Loyal"
    elif score >= 6:
        return "Potential"
    else:
        return "At Risk"

rfm['Segment'] = rfm['RFM_Score'].apply(assign_segment)

# Sidebar filters
segments = rfm['Segment'].unique().tolist()
selected_segment = st.sidebar.multiselect("Select Segment(s)", segments, default=segments)

filtered = rfm[rfm['Segment'].isin(selected_segment)]

# Metrics
st.metric("Total Customers", len(filtered))
st.metric("Average Monetary Value", f"${filtered['Monetary'].mean():,.2f}")

# Segment Distribution
st.subheader("📌 Segment Distribution")
seg_counts = filtered['Segment'].value_counts().sort_values(ascending=False)
st.bar_chart(seg_counts)

# Show table
st.subheader("📋 Customer Table")
st.dataframe(filtered.sort_values(by="RFM_Score", ascending=False))

# Footer
st.markdown("---")
st.caption("Built by Khwanchat | Dataset: UCI Online Retail")
