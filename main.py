# import modules.conversion as convert
# from conversion import distance_conversion

# count_gram = convert.gram(2)
# print(f"2 kg sama dengan {count_gram} gram")

# count_massa = convert.massa(2)
# print(f"2 kg sama dengan {count_massa} pound")

# count_ons = convert.ons(2)
# print(f"2 kg sama dengan {count_ons} ons")

# NUMPY
import numpy as np

data = [1, 2, 3, 4]
data2 = [[1, 2, 3], [2, 4, 6]]

vector_a = np.array(data)
matrix_a = np.array(data2)

print(vector_a)
print(matrix_a)
print(matrix_a.shape)
print(matrix_a.ndim)
