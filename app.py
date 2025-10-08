import pandas as pd
import pickle
import requests
from io import BytesIO
import streamlit as st

st.title("🛒 Shopper Spectrum App")

# ---------- Load files from Google Drive ----------
# Customer-product matrix
customer_product_matrix_url = "https://drive.google.com/uc?export=download&id=1ljmSkPlU8hq501ihSOndYQhoF4hyt40C"
customer_product_matrix = pd.read_csv(customer_product_matrix_url, index_col=0)

# Cosine similarity matrix
cosine_sim_url = "https://drive.google.com/uc?export=download&id=1RHjpx6wenYcTPBjHuIhVSMZisbcj7vFt"
cosine_sim_df = pd.read_csv(cosine_sim_url, index_col=0)

# RFM scaled data
rfm_scaled_url = "https://drive.google.com/uc?export=download&id=1lXoQs-XvUb3-Ee5KkKVWFMjes2W7LQ9N"
rfm_scaled = pd.read_csv(rfm_scaled_url, index_col=0)

# KMeans model
kmeans_url = "https://drive.google.com/uc?export=download&id=1Ja4bVkSyyw16s0H3-HmfsO4u0nq6KWHG"
response = requests.get(kmeans_url)
kmeans_model = pickle.load(BytesIO(response.content))

# ---------- Product Recommendation Module ----------
st.subheader("Product Recommendation")
product_name = st.text_input("Enter Product Name:")
if st.button("Get Recommendations"):
    if product_name in customer_product_matrix.columns:
        sim_scores = cosine_sim_df[product_name].sort_values(ascending=False).head(6)[1:]
        st.write("Recommended Products:", list(sim_scores.index))
    else:
        st.write("Product not found in dataset.")

# ---------- Customer Segmentation Module ----------
st.subheader("Customer Segmentation")
recency = st.number_input("Recency (days)")
frequency = st.number_input("Frequency (number of purchases)")
monetary = st.number_input("Monetary (total spend)")

if st.button("Predict Cluster"):
    import numpy as np
    from sklearn.preprocessing import StandardScaler

    # Prepare input
    input_df = pd.DataFrame([[recency, frequency, monetary]], columns=['Recency','Frequency','Monetary'])
    scaler = StandardScaler()
    scaler.fit(rfm_scaled[['Recency','Frequency','Monetary']])  # use your RFM scaler data
    input_scaled = scaler.transform(input_df)

    # Predict cluster
    cluster_label = kmeans_model.predict(input_scaled)[0]

    # Map cluster numbers to labels (adjust based on your project)
    cluster_mapping = {0:"High-Value", 1:"Regular", 2:"Occasional", 3:"At-Risk"}
    st.write("Predicted Segment:", cluster_mapping.get(cluster_label, "Unknown"))
