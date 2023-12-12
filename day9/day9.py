f = open("input.txt", "r")
lines = [[int(x) for x in line.strip().split(" ")] for line in f.read().split("\n")]

def extrapolate(line):
    if sum(i != 0 for i in line) == 0: return 0
    sub = []
    for i in range(len(line)-1):
        sub.append(line[i+1]-line[i])
    return line[-1] + extrapolate(sub)

print("Part 1 solution is", sum(extrapolate(line) for line in lines))
print("Part 2 solution is", sum(extrapolate(line[::-1]) for line in lines))