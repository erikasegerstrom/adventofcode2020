from pathlib import Path

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_9.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
input_data = []
for line in content:
    input_data.append(int(line))

def findPair(A, sum):
 
    # create an empty Hash Map
    dict = {}
 
    # do for each element
    for i, e in enumerate(A):
 
        # check if pair (e, sum-e) exists
 
        # if difference is seen before, print the pair
        if sum - e in dict:
            return True
 
        # store index of current element in the dictionary
        dict[e] = i
 
    # No pair with given sum exists in the list
    print(sum, " not found")
    return False
 
 
# Find pair with given sum in the list
if __name__ == '__main__':
    start = 0
    preamble = 25
    end = start + preamble
    A = input_data[start:end]
    number_to_find = input_data[end]
    findPair(A, number_to_find)
 
    while findPair(A, number_to_find) == True:
        start += 1
        end = start + preamble
        A = input_data[start:end]
        number_to_find = input_data[end]