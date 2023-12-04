with open("input.txt", "r") as file:
    matrix = [[char for char in line.strip()] for line in file]

ROWS = len(matrix)
COLS = len(matrix[0])

"""
find all numbers in tuple (value,(line,start,end)) and add to list
"""
numbers = []
for i in range(ROWS):
    j = 0
    while j < COLS:
        if matrix[i][j].isdecimal():
            start = j
            number = ""
            while j < COLS and matrix[i][j].isdecimal():
                number += matrix[i][j]
                j += 1
            j -= 1
            numbers.append((int(number), (i, start, j)))
        j += 1

"""
loop through numbers and check whether there is a special cahracter if yes add to sum
"""
sum = 0
for number in numbers:
    valid_number = False
    for i in range(number[1][0] - 1, number[1][0]+2):
        if i >= 0 and i < ROWS:
            for j in range(number[1][1] - 1, number[1][2] + 2):
                if j >= 0 and j < COLS:
                    if not(matrix[i][j].isdecimal() or matrix[i][j] == "."):
                        valid_number = True
                        sum += number[0]
                        break
            if valid_number:
                break

print("Part 1 solution is", sum)

"""
create dictionary of gears where key is tuple (x,y) and value is list of neighbour numbers
"""
gears = {}
for number in numbers:
    valid_number = False
    for i in range(number[1][0] - 1, number[1][0]+2):
        if i >= 0 and i < ROWS:
            for j in range(number[1][1] - 1, number[1][2] + 2):
                if j >= 0 and j < COLS:
                    if matrix[i][j] == "*":
                        if not gears.get((i,j)):
                            gears[(i,j)] = []
                        gears[(i,j)].append(number[0])

gear_ratio_sum = 0
def gear_ratio(gear):
    return gear[0]*gear[1]

for gear in gears:
    if len(gears[gear]) == 2:
        gear_ratio_sum += gear_ratio(gears[gear])

print("Part 2 solution is", gear_ratio_sum)