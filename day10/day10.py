file = open("test_input1.txt", "r")
grid = [[x for x in line] for line in file.read().split("\n")]
for y, line in enumerate(grid):
    if 'S' in line:
        start = (line.index('S'), y)
        break

print(start)

NORTH = (0,-1)
SOUTH = (0,1)
WEST = (-1,0)
EAST = (1,0)