# -------------------------------
# STEP 1: Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Better plot style

# -------------------------------
# STEP 2: Load Dataset
# -------------------------------
df = pd.read_csv("amazon.csv")  # Replace with your file name

# Quick overview
print("Dataset Info:\n", df.info())
print("\nFirst 5 rows:\n", df.head())

# -------------------------------
# STEP 3: Data Cleaning
# -------------------------------

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert numeric columns to float
numeric_cols = ['rating', 'discount_percentage', 'actual_price']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert, set errors to NaN

# Fill missing numeric values with mean
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# -------------------------------
# STEP 4: Exploratory Data Analysis (EDA)
# -------------------------------

# 4.1 Top 10 Categories by Number of Products
top_categories = df['category'].value_counts().head(10)
print("\nTop Categories:\n", top_categories)

# Convert top_categories to DataFrame for safer plotting
top_cat_df = top_categories.reset_index()
top_cat_df.columns = ['category', 'count']

# Bar plot for top categories
plt.figure(figsize=(10,5))
sns.barplot(x='category', y='count', data=top_cat_df, palette="viridis")
plt.title("Top 10 Product Categories")
plt.ylabel("Number of Products")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.show()

# 4.2 Average Rating & Discount per Category
category_summary = df.groupby('category')[['rating', 'discount_percentage']].mean().sort_values('rating', ascending=False)
print("\nCategory Summary (Average Rating & Discount):\n", category_summary)

# Heatmap of average rating per category
plt.figure(figsize=(8,5))
sns.heatmap(category_summary[['rating']], annot=True, cmap="YlGnBu")
plt.title("Average Rating by Category")
plt.show()

# 4.3 Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['rating'], bins=10, kde=True, color='orange')
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.show()

# 4.4 Discount vs Rating Scatter
plt.figure(figsize=(8,5))
sns.scatterplot(x='discount_percentage', y='rating', data=df, hue='category', alpha=0.7)
plt.title("Discount vs Rating")
plt.xlabel("Discount (%)")
plt.ylabel("Rating")
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
plt.show()

# 4.5 Top 10 Rated Products
top_products = df.sort_values('rating', ascending=False).head(10)
print("\nTop 10 Products by Rating:\n", top_products[['product_name', 'category', 'rating', 'actual_price']])

# 4.6 Price Category (High/Low) based on mean actual_price
df['price_category'] = df['actual_price'].apply(lambda x: 'High' if x > df['actual_price'].mean() else 'Low')
price_counts = df['price_category'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(price_counts, labels=price_counts.index, autopct='%1.1f%%', colors=['skyblue','lightgreen'])
plt.title("Price Category Distribution")
plt.show()

# -------------------------------
# STEP 5: Save Cleaned Dataset
# -------------------------------
df.to_csv("cleaned_amazon_products.csv", index=False)
print("Cleaned dataset saved as 'cleaned_amazon_products.csv'")

# -------------------------------
# STEP 6: Insights & Recommendations
# -------------------------------
print("\nINSIGHTS:")
print("1. Category with most products:", top_categories.idxmax())
print("2. Category with highest average rating:", category_summary['rating'].idxmax())
print("3. Category with highest average discount:", category_summary['discount_percentage'].idxmax())
print("4. Top-rated products:\n", top_products[['product_name','category','rating']])
print("5. Majority of products fall under", price_counts.idxmax(), "price category")



