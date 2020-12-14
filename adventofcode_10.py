from pathlib import Path
import numpy as np

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_10.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
input_data = []
for line in content:
    input_data.append(int(line))

# Add values to list and sort
input_data.append(0)
input_data.append(max(input_data)+3)
sorted_jolts = np.sort(np.array(input_data))

# Count dist
diff_dist = []
for i in range(len(sorted_jolts)-1):
    diff_dist.append(sorted_jolts[i+1] - sorted_jolts[i])

# Count unique values and multiply
(unique, counts) = np.unique(diff_dist, return_counts=True)
print('Result: ', np.prod(counts))