import pandas as pd

# Read the orders CSV directly into a DataFrame
df = pd.read_csv(r"C:\Users\vinay\Documents\Analytics-Project\data\orders_fresh.csv")

# Basic first-look commands
print("Shape (rows, columns):", df.shape)
print("\nColumn names:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())
