from pathlib import Path
import numpy as np
from graphs import Graph

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_10_test.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
input_data = []
for line in content:
    input_data.append(int(line))

# Add values to list and sort
input_data.append(0)
max_input = max(input_data)+3
input_data.append(max_input)
sorted_jolts = np.sort(np.array(input_data))

# Create dict
graph_dict = dict()
count_paths = 0
for count, jolt in enumerate(sorted_jolts):
    #print(count, jolt)
    graph_dict[jolt]= list()
    index = count + 1

    while index < len(sorted_jolts):
        if sorted_jolts[index] - jolt < 4:
            #print(jolt, sorted_jolts[index], sorted_jolts[index] - jolt)
            #print(graph_dict)
            graph_dict[jolt].extend([sorted_jolts[index]])
        index += 1

print(graph_dict)
print(count_paths)

graph = Graph(graph_dict)
result = graph.find_path(0, 22)
print(result)
result = graph.find_path(0, 22)
print(result)