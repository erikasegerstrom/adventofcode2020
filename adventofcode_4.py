import numpy as np

# Import data
f = open('input_data/adventofcode_input_4_1.txt', 'r')
content = f.readlines()
passports = {}
pass_nbr = 0
string = ''
mandatory_fields = ['pid:', 'ecl:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']

# Create dict
for line in content:
    if line == '\n':
        passports[pass_nbr] = string
        pass_nbr += 1
        string = ''
    else:
        string += line.strip()
passports[pass_nbr] = string

# Count valid passports
n_valid_passports = 0
for id in range(len(passports)):
    n_mandatory = 0
    for field in mandatory_fields:
        if field in passports[id]:
            n_mandatory +=1
    if n_mandatory == 7:
        n_valid_passports += 1

print('Number of passports: ', len(passports))
print('Number of valid passports: ', n_valid_passports)
