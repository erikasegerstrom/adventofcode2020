from pathlib import Path
from graphs import Graph

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_7_input.txt'
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

graph = Graph(bag_dict)
bag_to_find = 'shiny gold'
number_of_bags = 0
for key in bag_dict.keys():
    if graph.find_path(key, bag_to_find) != None and key != bag_to_find:
        number_of_bags += 1

print(number_of_bags)