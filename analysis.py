import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show first 5 rows
print("Dataset Preview:")
print(df.head())

# Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# Best selling product
best_product = df.groupby("Product")["Sales"].sum().idxmax()
print("\nBest Selling Product:", best_product)
