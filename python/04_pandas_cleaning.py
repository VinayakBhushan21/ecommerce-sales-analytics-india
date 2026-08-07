import pandas as pd

df_orders = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\orders_fresh.csv")
df_products = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\products.csv")
df_customers = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\customers.csv")

# --- GROUPBY: revenue per category (mirrors your SQL GROUP BY query) ---
merged = df_orders.merge(df_products, on="product_id", how="inner")
category_revenue = merged.groupby("category")["sales"].sum().round(2)
category_revenue = category_revenue.sort_values(ascending=False)
print(category_revenue)

# --- GROUPBY with multiple aggregations at once ---
category_summary = merged.groupby("category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    order_count=("order_id", "count")
).round(2)
print(category_summary)

# --- MERGE: mirrors your SQL LEFT JOIN "customers with no orders" query ---
customer_order_check = df_customers.merge(
    df_orders, on="customer_id", how="left", indicator=True
)
customers_no_orders = customer_order_check[customer_order_check["_merge"] == "left_only"]
print(f"Customers with zero orders: {customers_no_orders['customer_id'].nunique()}")

# --- FINDING missing values ---
print(df_orders.isnull().sum())          # count of missing values per column

# --- FIXING missing values ---
df_orders["payment_mode"] = df_orders["payment_mode"].fillna("Unknown")

# --- FINDING duplicates ---
print("Duplicate rows found:", df_orders.duplicated().sum())

# --- FIXING duplicates ---
df_orders = df_orders.drop_duplicates()
print("Shape after removing duplicates:", df_orders.shape)

# --- FIXING inconsistent text casing ---
df_orders["city"] = df_orders["city"].str.title()   # "MUMBAI" -> "Mumbai"

# --- Save the cleaned file ---
df_orders.to_csv(
    r"C:\Users\vinay\Documents\Analytics-Project\data\orders_cleaned.csv",
    index=False
)
print("Cleaned file saved.")