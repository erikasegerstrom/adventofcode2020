from pathlib import Path
from graphs import Graph

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_7_input_test.txt'
f = open(input_file, 'r')
content = f.readlines()

bag_dict = dict()
for line in content:
    split_line = line.split()
    bag_type = split_line[0] + ' ' + split_line[1]
    bag_dict[bag_type] = list()
    index = 5
    if split_line[4] != 'no':
        while index < len(split_line):
            bag_dict[bag_type].extend([split_line[index] + ' ' + split_line[index+1]])
            index += 4

print(bag_dict)
#graph = Graph(bag_dict)
"""
# droppa key = shiny gold?
all_possible_bags = []
bag_to_find = 'shiny gold'
for key in bag_dict.keys():
    sub_bags = bag_dict[key]
    if bag_to_find in sub_bags:
        all_possible_bags.append(key)
    else:
        for value in sub_bags:
            if bag_to_find in bag_dict[value]:
                print(key, value)
                all_possible_bags.append(key)

def search_bags(bag_dict, bag_to_find, list_append):
    for key in bag_dict.keys():


all_possible_bags = list(set(all_possible_bags))
n_bags = len(all_possible_bags)
print('Number of bags: ', n_bags)"""