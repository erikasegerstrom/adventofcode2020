# Import data
f = open('adventofcode_input_6.txt', 'r')
content = f.readlines()

sum_intersect = 0
first_line = True
for line in content:
    if first_line:
        string = line.strip()
        string_concat_unique = list(set(string))
        first_line = False
    elif line == '\n':
        string_concat_unique = list(set(string) & set(string_concat_unique))
        sum_intersect += len(string_concat_unique)
        first_line = True
    else:
        string = line.strip()    
        string_concat_unique = list(set(string) & set(string_concat_unique))

string_concat_unique = list(set(string) & set(string_concat_unique))
sum_intersect += len(string_concat_unique)

print('Sum intersections: ', sum_intersect)