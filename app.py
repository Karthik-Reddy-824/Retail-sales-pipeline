import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('db/sales.db')

# Load data
orders = pd.read_sql("SELECT * FROM orders", conn)
products = pd.read_sql("SELECT * FROM products", conn)
print(orders.tail())

st.title("📊 Retail Sales Dashboard")

# KPI
total_revenue = orders['Revenue'].sum()
st.metric("Total Revenue", f"${total_revenue:,.2f}")

# Revenue by Region
region_df = orders.groupby('Region')['Revenue'].sum()
st.bar_chart(region_df)

# Monthly Revenue Trend
orders['Order Date'] = pd.to_datetime(orders['Order Date'])
monthly_revenue = (orders.groupby(orders['Order Date'].dt.to_period('M'))['Revenue'].sum())
monthly_revenue.index = monthly_revenue.index.astype(str)
st.subheader("📈 Monthly Revenue Trend")
st.line_chart(monthly_revenue)

# Top 10 Products by Revenue
top_products = (orders.groupby('Product ID')['Revenue'].sum().sort_values(ascending=False).head(10))
fig, ax = plt.subplots(figsize=(10, 6))

top_products.sort_values().plot(kind='barh',ax=ax)
ax.set_title("🏆 Top 10 Products by Revenue")
ax.set_xlabel("Revenue")
ax.set_ylabel("Product ID")
st.pyplot(fig)

# Merge orders and products tables
merged_df = orders.merge(products,on='Product ID',how='left')

# Revenue by Category
category_revenue = (merged_df.groupby('Category')['Revenue'].sum().sort_values(ascending=False))
st.subheader("📊 Revenue by Category")
st.bar_chart(category_revenue)