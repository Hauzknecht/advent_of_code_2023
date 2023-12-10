import math

file = open("input.txt", "r")
instructions, nodes = file.read().split("\n\n")
nodes = { line[0:3]:(line[7:10],line[12:15]) for line in nodes.split("\n")}
"""
current="AAA"
step = 0

while current != 'ZZZ':
    if instructions[step%len(instructions)] == "L":
        current = nodes[current][0]
    else:
        current = nodes[current][1]
    step += 1
print(step)
"""
current = []
for node in nodes.keys():
    if node[2] == 'A':
        current.append(node)
print(current)

def count_steps(node):
    tmp = node
    step = 0
    while tmp[2] != 'Z':
        if instructions[step%len(instructions)] == "L":
            tmp = nodes[tmp][0]
        else:
            tmp = nodes[tmp][1]
        step +=1
    return step

steps = []
for node in current:
    steps.append(count_steps(node))
print(math.lcm(steps))