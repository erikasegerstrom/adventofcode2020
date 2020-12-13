from pathlib import Path
import copy

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_8.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
instructions_input = list()
for line in content:
    instructions_input.append(line.split())

def run_instructions(instructions):
    """
    Run instruction file
    """
    index = 0
    accumulator = 0
    index_visited = list()

    while index not in index_visited:
        index_visited.append(index)
        instruction = instructions[index][0]
        argument = int(instructions[index][1])

        # Apply instruction
        if instruction == 'nop':
            index += 1
        elif instruction == 'jmp':
            index += argument
        elif instruction == 'acc':
            accumulator += argument
            index += 1
    
        # Check outcome
        if index in index_visited:
            return False, 0
        elif index == len(content):
            return True, accumulator

for i in range(len(content)):
    instructions_updated = copy.deepcopy(instructions_input)
    instruction = instructions_input[i][0]

    # Update instruction
    if instruction == 'nop':
        instructions_updated[i][0] = 'jmp'
    elif instruction == 'jmp':
        instructions_updated[i][0] = 'nop'

    # Run
    success, acc_result = run_instructions(instructions_updated)

    if success == True:
        print('Row ', i, ' has been changed and completed successfully!')
        print('Accumulator value: ', acc_result)
        exit()
