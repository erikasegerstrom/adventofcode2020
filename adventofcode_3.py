import numpy as np
f = open('input_data/adventofcode_input_3_1.txt', 'r')
content = f.read()

arr  = list(filter(lambda a: a != '\n', list(content)))

n_elements = len(arr)
n_rows = int(len(arr)/31)
n_columns = 31

matrix = np.array([['.'] * n_columns] * n_rows)

row = 0
element_idx = 0
while row < n_rows:
    column = 0
    while column < n_columns:
        matrix[row][column] = arr[element_idx]
        element_idx += 1
        column += 1
    row += 1


def count_trees(matrix, n_rows, right, down):
    row = 0
    column = 0
    n_trees = 0
    while row < n_rows:
        element = matrix[row][column]
        if element == '#':
            n_trees += 1
        row += down
        column = (column + right) % 31
    return n_trees

first = count_trees(matrix, n_rows, 1, 1)
second = count_trees(matrix, n_rows, 3, 1)
third = count_trees(matrix, n_rows, 5, 1)
fourth = count_trees(matrix, n_rows, 7, 1)
fifth = count_trees(matrix, n_rows, 1, 2)
print('First count: ', first)
print('Second count: ', second)
print('Third count: ', third)
print('Fourth count: ', fourth)
print('Fifth count: ', fifth)
print('Solution: ', first*second*third*fourth*fifth)