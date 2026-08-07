import pandas as pd

df = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\orders_fresh.csv")

# --- Series vs DataFrame ---
sales_series = df["sales"]          # a single column = a Series
print(type(sales_series))
print(type(df))

# --- First-look commands ---
print(df.shape)                     # (rows, columns)
print(df.columns)                   # column names
print(df.head(5))                   # first 5 rows
print(df.tail(5))                   # last 5 rows
print(df.info())                    # column types + non-null counts
print(df.describe())                # summary stats for numeric columns

# --- Filtering (Pandas equivalent of SQL WHERE) ---
delivered_orders = df[df["order_status"] == "Delivered"]
print(delivered_orders.shape)

high_value = df[(df["sales"] > 10000) & (df["order_status"] == "Delivered")]
print(high_value.shape)

# --- Sorting ---
top_orders = df.sort_values(by="sales", ascending=False)
print(top_orders.head(5))

# --- loc vs iloc ---
print(df.loc[0])                    # row with LABEL/index 0
print(df.loc[0, "sales"])           # label-based: row 0, column "sales"
print(df.iloc[0])                   # row at POSITION 0 (same result here, but by position)
print(df.iloc[0:5, 0:3])            # first 5 rows, first 3 columns, by position