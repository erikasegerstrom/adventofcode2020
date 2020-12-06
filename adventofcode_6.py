# Import data
f = open('adventofcode_input_6.txt', 'r')
content = f.readlines()

string = ''
sum_unique = 0

# Create dict
for line in content:
    if line == '\n':
        string2 = list(set(string))
        sum_unique += len(string2)
        string = ''
    else:
        string += line.strip()

string2 = list(set(string))
sum_unique += len(string2)
print(sum_unique)