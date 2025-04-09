import pandas as pd

df_sales = pd.read_csv("supermarket_sales.csv")
print("Data: \n")
print(df_sales, "\n")
print(df_sales.columns, "\n")
print(df_sales.iloc[15], "\n")
print(df_sales.iloc[15:20], "\n")
print(df_sales.describe(), "\n")
print(df_sales.isnull().values.any(), "\n")

df_clean = df_sales.dropna()
print(df_clean.isnull().values.any(), "\n")
print(df_clean.describe(), "\n")

total_beli = df_clean["Quantity"].sum()
df_percen = (df_clean["Quantity"]/total_beli)*100

new_df = pd.DataFrame({"Invoice ID": df_clean["Invoice ID"], "Percen": df_percen})

print(new_df)

merge_df = pd.merge(df_clean, new_df, on="Invoice ID")

print(merge_df, "\n")

pivot_1 = pd.pivot_table(merge_df, values="Invoice ID", columns="Gender", aggfunc="count")

print(pivot_1)