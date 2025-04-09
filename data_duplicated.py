import pandas as pd

# dataframe pertama
data1 = pd.DataFrame({
  "Nama": ["Jhon", "Anna", "Pieter", "Linda"] * 2,
  "Usia": [30, 35, 40, 45] * 2
})

print(data1)