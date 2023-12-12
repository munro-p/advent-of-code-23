'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
read in file
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def read_file(filename):
    
    file = open(filename)
    file_lines = [[char for char in line.strip("\n")] for line in file.readlines()]

    return file_lines


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
main
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
galaxies = read_file("input-1.txt")
galaxies_transposed = list(map(list, zip(*galaxies)))

'''
work out columns and rows to expand
'''
rows_to_expand = []
columns_to_expand = []

for index,line in enumerate(galaxies):
    if("#" not in line):
        rows_to_expand.append(index)

for index, line in enumerate(galaxies_transposed):
    if("#" not in line):
        columns_to_expand.append(index)

''' 
add the rows 
'''
append_to_row_index = 0;
for index in rows_to_expand:
    galaxies.insert(index + append_to_row_index, ["." for char in galaxies[0]])
    append_to_row_index = append_to_row_index + 1


''' 
add the columns 
'''
append_to_col_index = 0;
for index in columns_to_expand:    
    for line in galaxies:
        line.insert(index + append_to_col_index, ".")
    append_to_col_index = append_to_col_index + 1;

'''
get coords of all the galaxies
'''
found = []
for i, sublist in enumerate(galaxies):
    for j, item in enumerate(sublist):
        if item == "#":
            found.append([i,j])
 
'''
and now compare the distances and add them up
'''
total = 0
for start in found:
    for compare in found:
        if start == compare:
            break
        summed = abs(start[0]-compare[0]) +  abs(start[1]-compare[1])
        total = total + summed

print(total)
