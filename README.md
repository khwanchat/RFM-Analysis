# 📊 RFM Segmentation Dashboard

This project is an interactive Streamlit dashboard for segmenting customers using the **RFM (Recency, Frequency, Monetary)** model. It helps identify valuable customer groups for targeted CRM, retention, and loyalty campaigns.

---

## 📌 Key Features

- Load and clean the UCI Online Retail dataset
- Calculate RFM scores for each customer
- Assign customer segments like **Champions**, **Loyal**, **At Risk**
- Interactive dashboard with:
  - Sidebar segment filters
  - Customer KPIs (Total Count, Avg. Monetary)
  - Segment distribution chart
  - Detailed customer-level table
- Built with `Streamlit`, `pandas`, `matplotlib`, and `seaborn`

---

## 📁 Files Included

- `rfm_scores.csv` – Cleaned RFM dataset
- `RFM_Dashboard_App.py` – Streamlit dashboard code
- `rfm_data_prep.ipynb` – Jupyter Notebook for data preparation
- `requirements.txt` – Python dependencies

  📁 Data Source
Dataset: Online Retail Listing on Kaggle
https://www.kaggle.com/datasets/ilkeryildiz/online-retail-listing
Source: UCI Machine Learning Repository

---

## 🚀 How to Run the App

1. **Clone the repository**  
```bash
git clone https://github.com/khwanchat/RFM-Segmentation-Dashboard.git
cd RFM-Segmentation-Dashboard
