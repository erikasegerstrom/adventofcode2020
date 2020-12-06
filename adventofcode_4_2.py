import numpy as np
from collections import defaultdict

# Import data
f = open('adventofcode_input_4_1.txt', 'r')
content = f.readlines()
passports = defaultdict(dict)
pass_nbr = 0
string = ''
mandatory_fields = ['pid', 'ecl', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

# Create dict 
for line in content:
    if line == '\n':
        for field in mandatory_fields:
            passports[pass_nbr][field] = None
            split_string = string.split()
            for element in split_string:
                if field in element:
                    passports[pass_nbr][field] = element[4:]                
        pass_nbr += 1        
        string = ''
    else:
        string += line

# Inkludera sista!
for field in mandatory_fields:
    passports[pass_nbr][field] = None
    split_string = string.split()
    for element in split_string:
        if field in element:
            passports[pass_nbr][field] = element[4:]                

def check_validity(key, value):
    if value == None:
        return False
    elif key == 'byr' and (1920 <= int(value) <= 2002):
        return True
    elif key == 'iyr' and (2010 <= int(value) <= 2020):
        return True
    elif key == 'eyr' and (2020 <= int(value) <= 2030):
        return True
    elif key == 'hgt':
        if value.find('cm') > -1:
            height = value[:value.find('cm')]
            if 150 <= int(height) <= 193:
                return True
            else:
                return False
        elif value.find('in') > -1:
            height = value[:value.find('in')]
            if 59 <= int(height) <= 76:
                return True
            else:
                return False
        else:
            return False
    elif key == 'hcl' and value[:1] == '#' and len(value) == 7:
        return True
    elif key == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    elif key == 'pid' and len(value) == 9 and value.isdigit():
        return True
    else:
        return False

# Count valid passports
n_valid_passports = 0
for key in passports.keys():
    valid_flg = True
    for secondKey in passports[key].keys():
        valid = check_validity(secondKey, passports[key][secondKey])
        if valid == False:
            valid_flg = False
    if valid_flg:
        n_valid_passports += 1

print('Number of passports: ', len(passports))
print('Number of valid passports: ', n_valid_passports)