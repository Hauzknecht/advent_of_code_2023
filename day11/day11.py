file = open("input.txt", "r")
lines = [line.strip() for line in file]

def solve(expansion_factor):
    ROWS = len(lines)
    COLS = len(lines[0])
    multiply_factor = expansion_factor -1
    empty_columns = set(range(COLS))
    empty_rows = set(range(ROWS))
    galaxies = set()

    for i ,line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.add((i, j))
                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_columns:
                    empty_columns.remove(j)

    distances = {}
    for i1, j1 in galaxies:
        for i2, j2 in galaxies:
            pair = frozenset({(i1, j1), (i2, j2)})
            if (i1, j1) != (i2, j2) and pair not in distances:
                distance = abs(i2-i1) + abs(j2-j1)
                empty_rows_between = [i for i in range(*sorted([i1, i2])) if i in empty_rows]
                empty_columns_between = [i for i in range(*sorted([j1, j2])) if i in empty_columns]
                adjusted_distance = distance + multiply_factor * (len(empty_columns_between) + len(empty_rows_between))
                distances[pair] = adjusted_distance
    
    return sum(distances.values())

print("Part1 solution is", solve(2))
print("Part2 solution is", solve(1000000))