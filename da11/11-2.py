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
get coords of all the galaxies
'''
found = []
for i, sublist in enumerate(galaxies):
    for j, item in enumerate(sublist):
        if item == "#":
            found.append([j,i])
 

print(found)
'''
and now figure out the new totals based on the existing points and the places where you should expand
'''
total = 0
to_add = 999999

for start in found:
    for compare in found:
        if start == compare:
            break

        summed = abs(start[0]-compare[0]) +  abs(start[1]-compare[1])
       
        # are there any rows to expand
        x1 = (start[0])
        x2 = (compare[0])
        if(x1 > x2):
            for i in range(x2, x1):
                if(i in columns_to_expand):
                    total = total + to_add
        else:
            for i in range(x1, x2):
                if(i in columns_to_expand):
                    total = total + to_add
        
        # are there any columns to expand
        y1=(start[1])
        y2=(compare[1])
        if(y1 > y2):
            for i in range(y2, y1):
                if(i in rows_to_expand):
                    total = total + to_add
        else:
            for i in range(y1, y2):
                if(i in rows_to_expand):
                    total = total + to_add
        
        
    
        total = total + summed

print(total)
