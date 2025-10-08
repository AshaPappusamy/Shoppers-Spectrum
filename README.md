🛒 Shopper Spectrum: Customer Segmentation and Product Recommendations in E-Commerce
🎯 Project Overview

The Shopper Spectrum project focuses on analyzing e-commerce transaction data to gain actionable insights into customer purchasing behavior. Using RFM (Recency, Frequency, Monetary) analysis and unsupervised learning, the project segments customers into meaningful groups for targeted marketing. Additionally, it implements an item-based collaborative filtering recommendation system to suggest similar products, enhancing customer experience and driving business growth.

This project demonstrates the end-to-end pipeline of data cleaning, feature engineering, clustering, and recommendation, along with a Streamlit web application for real-time interaction.

🧠 Key Objectives

Segment customers based on RFM (Recency, Frequency, Monetary) metrics using K-Means Clustering

Identify high-value, regular, and at-risk customers

Develop a collaborative filtering-based recommendation system using Cosine Similarity

Deploy an interactive Streamlit app to:

Predict customer segment based on input RFM values

Recommend similar products for any given product

📦 Dataset Description
Column	Description
InvoiceNo	Transaction number
StockCode	Unique product/item code
Description	Name of the product
Quantity	Number of products purchased
InvoiceDate	Date and time of transaction
UnitPrice	Price per product
CustomerID	Unique identifier for each customer
Country	Country where the customer is based

Dataset Source: Public e-commerce dataset (2022–2023)

🧰 Tools & Technologies

Programming: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

Techniques: RFM Analysis, K-Means Clustering, Collaborative Filtering

Similarity Metric: Cosine Similarity

Deployment: Streamlit

Version Control: GitHub

📊 Workflow

Data Preprocessing:

Removed missing CustomerIDs

Excluded cancelled transactions

Filtered negative/zero quantities and prices

Computed total amount per transaction

Feature Engineering (RFM):

Recency = Days since last purchase

Frequency = Number of transactions per customer

Monetary = Total spending per customer

Clustering:

Standardized RFM features

Used Elbow Method and Silhouette Score to choose optimal clusters

Interpreted segments (High-Value, Regular, Occasional, At-Risk)

Recommendation System:

Built a Customer–Product matrix

Computed Cosine Similarity between products

Suggested top 5 similar products for any given product

Deployment:

Developed an interactive Streamlit web app

Module 1: Product Recommendation

Module 2: Customer Segmentation Prediction

🎯 Business Impact

📌 Targeted Marketing: Identify high-value customers for loyalty campaigns

📌 Customer Retention: Detect at-risk customers and re-engage them

📌 Personalization: Recommend relevant products to boost sales

📌 Inventory Planning: Understand demand patterns by cluster

💡 Insights

Customers show distinct buying behaviors based on RFM

A small percentage of customers contribute major revenue (Pareto effect)

Product similarity analysis helps cross-sell and upsell relevant items

🚀 Streamlit App Features

🧠 Product Recommendation Module

Input: Product name

Output: Top 5 similar products

👥 Customer Segmentation Module

Input: Recency, Frequency, Monetary

Output: Predicted customer cluster (High-Value / Regular / At-Risk / Occasional)

🧩 Project Deliverables

✅ Cleaned & processed dataset

✅ EDA with visual insights

✅ RFM-based customer segmentation

✅ Collaborative filtering-based product recommendation

✅ Streamlit web application

✅ GitHub repository with code, app, and documentation

🏁 Conclusion

This project successfully demonstrates how unsupervised learning and recommendation algorithms can be leveraged to enhance customer experience and business strategy in e-commerce. By segmenting customers and recommending similar products, businesses can implement personalized marketing, retention programs, and data-driven decision-making.
