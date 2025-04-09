import pandas as pd

# example data
data = {
  "Tanggal": ["2022-01-01", "2022-01-01", "2022-01-02", "2022-01-012", "2022-01-03"],
  "Barang": ["Anggur", "Apel", "Jambu", "Pisang", "Duku"],
  "Penjualan": [100, 200, 150, 250, 180]
}

df = pd.DataFrame(data)

print("Data salses")

print(df)

print("""
      """)

# pivot table
pivot_table = pd.pivot_table(df, values="Penjualan", index="Tanggal", columns="Barang", aggfunc="sum")

print("Tabel pivot:")

print(pivot_table)


print("""
      """)

# table pivot from filter data
filter_df = df[df["Barang"].isin(["Anggur", "Apel", "Jambu"])]

# print table pivot from filter data
pivot_table = pd.pivot_table(filter_df, values="Penjualan", index="Tanggal", columns="Barang", aggfunc="sum")

print("Tabel pivot berdasarkan filter:")

print(pivot_table)