import pandas as pd

# dataframe 1
data1 = {
  "ID": [1, 2, 3, 4],
  "Nama": ["Jhon", "Anna", "Pieter", "Linda"],
  "Usia": [30, 35, 40, 45]
}

df1 = pd.DataFrame(data1)

# dataframe 1
data2 = {
  "ID": [1, 2, 5],
  "Kota": ["Jakarta", "Bandung", "Surabaya"]
}

df2 = pd.DataFrame(data2)

# merged data based on ID
merged_df = pd.merge(df1, df2, on="ID", how="outer")

# show merged data
print("Hasil penggabungan data:")
print(merged_df)

# reshape
reshape = df1.stack()
print(reshape)