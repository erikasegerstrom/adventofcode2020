def import_data():
    text_file = open("input_data/adventofcode_1_1_input.txt", "r")
    lines = text_file.read().split('\n')
    return lines

input = import_data()

input = list(map(int, input))

def run_1_1(input):
    """
    First puzzle
    """
    for nbr in input:
        residual = 2020 - nbr
        if residual in input:
            print('Solution: ', residual * nbr)


def run_1_2(input):
    """
    Second puzzle
    """
    length  = range(len(input))
    for i in length:
        j = i + 1
        while j < len(input):
            residual = 2020 - (input[i] + input[j])
            if residual in input:
                print('Solution: ', input[i]*input[j]*residual)
                exit()
            j += 1

run_1_1(input)
run_1_2(input)