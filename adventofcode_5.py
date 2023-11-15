# Import data
f = open('input_data/adventofcode_input_5_1.txt', 'r')
content = f.readlines()

n_rows = 128
n_columns = 8
seat_id = dict()
seat_index = 0

for line in content:
    row_min = 0
    row_max = 127
    column_min = 0
    column_max = 7
    boarding = line.strip()

    # Find row
    for i in range(7):
        if line[i] == 'F':
            row_max = row_min + (row_max - row_min + 1)/2 - 1
        elif line[i] == 'B':
            row_min = row_min + (row_max - row_min + 1)/2

    # Find column
    for i in range(3):
        if line[i+7] == 'R':
            column_min = column_min + (column_max - column_min + 1) /2
        elif line[i+7] == 'L':
            column_max = column_min + (column_max - column_min + 1) /2 -1
    seat_id[seat_index] = row_min * 8 + column_min
    seat_index += 1
print(max(seat_id.values()))

new = dict(sorted(seat_id.items(), key=lambda item: item[1]))
array = []
for key in new.keys():
    array.append(int(new[key]))

def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

print(missing_elements(array))