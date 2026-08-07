import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\orders_cleaned.csv")
df_products = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\products.csv")
df_returns = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\returns.csv")

# Convert order_date to a real datetime column (it loaded as text)
df["order_date"] = pd.to_datetime(df["order_date"])

# Only analyze delivered orders as "real" completed sales
delivered = df[df["order_status"] == "Delivered"]

# --- CHART 1: Monthly revenue trend (line chart) ---
monthly_revenue = delivered.set_index("order_date")["sales"].resample("ME").sum()

plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig(r"C:\Users\vinay\Documents\Analytics-Project\reports\monthly_revenue_trend.png")
plt.show()

# --- CHART 2: Revenue by category (bar chart) ---
merged = delivered.merge(df_products, on="product_id", how="inner")
category_revenue = merged.groupby("category")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
category_revenue.plot(kind="bar", color="steelblue")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\vinay\Documents\Analytics-Project\reports\revenue_by_category.png")
plt.show()

# --- CHART 3: Return rate by category ---
returns_merged = df_returns.merge(df, on="order_id", how="left").merge(df_products, on="product_id", how="left")
returns_by_category = returns_merged.groupby("category")["order_id"].count()
total_orders_by_category = merged.groupby("category")["order_id"].count()
return_rate = (returns_by_category / total_orders_by_category * 100).round(2).sort_values(ascending=False)

plt.figure(figsize=(10, 5))
return_rate.plot(kind="bar", color="indianred")
plt.title("Return Rate (%) by Category")
plt.xlabel("Category")
plt.ylabel("Return Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\vinay\Documents\Analytics-Project\reports\return_rate_by_category.png")
plt.show()

# --- CHART 4: Payment mode distribution (pie chart) ---
payment_dist = df["payment_mode"].value_counts()

plt.figure(figsize=(7, 7))
payment_dist.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Mode Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(r"C:\Users\vinay\Documents\Analytics-Project\reports\payment_mode_distribution.png")
plt.show()