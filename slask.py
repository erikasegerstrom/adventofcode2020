import numpy as np
n_rows = 3
n_columns = 4
matrix = np.array([[0] * n_columns] * n_rows)
print(matrix)
matrix[0][0] = 5
print(matrix)