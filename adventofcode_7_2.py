from pathlib import Path
from graphs import Graph
from collections import defaultdict

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_7_input_test.txt'
f = open(input_file, 'r')
content = f.readlines()

bag_dict = defaultdict(dict)
for line in content:
    split_line = line.split()
    bag_type = split_line[0] + ' ' + split_line[1]
    #bag_dict[bag_type][] = list()  
    index = 4
    if split_line[4] != 'no':
        while index < len(split_line):
            n_sub_bags = int(split_line[index])
            sub_bag = [split_line[index+1] + ' ' + split_line[index+2]]
            bag_dict[bag_type][sub_bag].extend([n_sub_bags])
            index += 4
print(bag_dict)
"""
graph = Graph(bag_dict)
bag_to_find = 'shiny gold'
number_of_bags = 0
for key in bag_dict.keys():
    if graph.find_path(key, bag_to_find) != None and key != bag_to_find:
        number_of_bags += 1

print(number_of_bags)"""