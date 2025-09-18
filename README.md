# 📊 Amazon Sales & Customer Insights Dashboard

## 🔹 Project Overview
This project analyzes an Amazon product dataset to uncover insights about **sales trends, customer behavior, and discount strategies**.  
It demonstrates end-to-end **data cleaning, exploratory data analysis (EDA), and visualization** — core skills for any Data Analyst role.

---

## 🔹 Dataset
- **Source:** Amazon products dataset (CSV file provided).  
- **Size:** ~X rows, Y columns (after cleaning).  
- **Key Columns:**  
  - `product_name` – Name of the product  
  - `discounted_price` – Final selling price  
  - `actual_price` – Original price  
  - `discount_percentage` – Discount offered  
  - `rating` – Customer rating  
  - `rating_count` – Number of ratings (used as proxy for sales popularity)  
  - `main_category` – Product category  

---

## 🔹 Tech Stack
- **Python** → Data cleaning, analysis (Pandas, NumPy)  
- **Matplotlib & Seaborn** → Data visualization  
- **SQL (optional)** → Querying cleaned dataset  
- **Streamlit** → Dashboard building (optional extension)

---

## 🔹 Data Cleaning
Steps performed:
1. Converted `discounted_price` and `actual_price` from strings like `₹399` → numeric `399`.  
2. Converted `discount_percentage` from `"64%"` → numeric `64`.  
3. Converted `rating` to float.  
4. Converted `rating_count` from `"24,269"` → `24269`.  
5. Extracted `main_category` from `category` column.  

✅ Final cleaned dataset saved as **`amazon_cleaned.csv`**.

---

## 🔹 Exploratory Data Analysis (EDA)
Key questions explored:
- Which are the **top 10 categories** by number of products?  
- What are the **average ratings and discounts per category**?  
- How are **discounts distributed** across products?  
- Do higher discounts mean higher sales (rating_count)?  
- Which products are the **most popular** and **best-rated**?

---

## 🔹 Key Insights
- **Clothing & Electronics** dominate product listings.  
- Average discount across products was **~45%**, but heavy discounts did not always correlate with high ratings.  
- Some categories like **Books** maintained very high ratings even with lower discounts.  
- Identified **top-selling categories & products** based on rating count.  

---

## 🔹 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/amazon-sales-insights.git
   cd amazon-sales-insights

