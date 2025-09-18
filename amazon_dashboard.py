# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# -------------------------------
# LOAD CLEANED DATA
# -------------------------------
df = pd.read_csv("cleaned_amazon_products.csv")  # cleaned dataset

# Ensure numeric columns
numeric_cols = ['rating', 'discount_percentage', 'actual_price']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col].fillna(df[col].mean(), inplace=True)

# -------------------------------
# STREAMLIT LAYOUT
# -------------------------------
st.title("📊 Amazon Product Analysis Dashboard")
st.markdown("Interactive analysis of Amazon products with category filters, insights, and visualizations!")

# -------------------------------
# SIDEBAR CATEGORY FILTER
# -------------------------------
categories = df['category'].unique()
selected_category = st.sidebar.selectbox("Select Category", np.append(["All"], categories))

if selected_category != "All":
    data = df[df['category'] == selected_category]
else:
    data = df.copy()

# -------------------------------
# SHOW TOP 10 CATEGORIES
# -------------------------------
st.subheader("Top 10 Categories by Number of Products")
top_categories = df['category'].value_counts().head(10)
top_cat_df = top_categories.reset_index()
top_cat_df.columns = ['category', 'count']

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x='category', y='count', data=top_cat_df, palette="viridis", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# HEATMAP: Average Rating & Discount
# -------------------------------
st.subheader("Average Rating & Discount per Category")
category_summary = df.groupby('category')[['rating','discount_percentage']].mean()
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.heatmap(category_summary, annot=True, cmap="YlGnBu", ax=ax2)
st.pyplot(fig2)

# -------------------------------
# RATING DISTRIBUTION
# -------------------------------
st.subheader("Rating Distribution")
fig3, ax3 = plt.subplots(figsize=(8,5))
sns.histplot(data['rating'], bins=10, kde=True, color='orange', ax=ax3)
st.pyplot(fig3)

# -------------------------------
# DISCOUNT VS RATING SCATTER
# -------------------------------
st.subheader("Discount vs Rating")
fig4, ax4 = plt.subplots(figsize=(8,5))
sns.scatterplot(x='discount_percentage', y='rating', data=data, hue='category', alpha=0.7, ax=ax4)
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
st.pyplot(fig4)

# -------------------------------
# PRICE CATEGORY PIE CHART
# -------------------------------
st.subheader("Price Category Distribution")
data['price_category'] = data['actual_price'].apply(lambda x: 'High' if x > df['actual_price'].mean() else 'Low')
price_counts = data['price_category'].value_counts()

fig5, ax5 = plt.subplots(figsize=(6,6))
ax5.pie(price_counts, labels=price_counts.index, autopct='%1.1f%%', colors=['skyblue','lightgreen'])
st.pyplot(fig5)

# -------------------------------
# TOP 10 PRODUCTS TABLE
# -------------------------------
st.subheader("Top 10 Products by Rating")
top_products = data.sort_values('rating', ascending=False).head(10)
st.table(top_products[['product_name','category','rating','actual_price','discount_percentage']])

# -------------------------------
# KEY INSIGHTS
# -------------------------------
st.subheader("Key Insights")
st.write(f"**Category with most products:** {df['category'].value_counts().idxmax()}")
st.write(f"**Category with highest average rating:** {category_summary['rating'].idxmax()}")
st.write(f"**Category with highest average discount:** {category_summary['discount_percentage'].idxmax()}")
st.write(f"**Majority of products fall under price category:** {df['actual_price'].apply(lambda x: 'High' if x > df['actual_price'].mean() else 'Low').value_counts().idxmax()}")

# -------------------------------
# DOWNLOAD BUTTON FOR CLEANED DATA
# -------------------------------
st.subheader("Download Cleaned Data")
csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='amazon_products_filtered.csv',
    mime='text/csv',
)
