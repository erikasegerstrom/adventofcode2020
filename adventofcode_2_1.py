import re

def import_data():
    text_file = open("input_data/adventofcode_2_1_input.txt", "r")
    lines = text_file.read().split('\n')
    return lines

input = import_data()

# First puzzle
n_correct = 0
for element in input:
    parsed = re.split('[: -]', element)
    n_occurance = parsed[4].count(parsed[2])
    if int(parsed[0]) <= n_occurance <= int(parsed[1]):
        n_correct += 1

print('Number of correct pwds: ', n_correct)

# Second puzzle
n_correct = 0
for element in input:
    parsed = re.split('[: -]', element)
    char = parsed[2]
    first = parsed[4][int(parsed[0])-1]
    second = parsed[4][int(parsed[1])-1]
    if (first == char and second != char) or (first != char and second == char):
        n_correct += 1
print('Number of correct pwds: ', n_correct)