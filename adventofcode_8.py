from pathlib import Path

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_8.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
instructions = list()
for line in content:
    instructions.append(line.split())

index = 0
accumulator = 0
index_visited = list()
while index not in index_visited:
    index_visited.append(index)
    argument = int(instructions[index][1])
    if instructions[index][0] == 'nop':
        index += 1
    elif instructions[index][0] == 'jmp':
        index += argument
    elif instructions[index][0] == 'acc':
        accumulator += argument
        index += 1
    if index in index_visited:
        print('Accumulator: ', accumulator)