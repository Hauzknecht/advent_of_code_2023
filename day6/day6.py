file = open("input.txt", "r")
t, d = file.read().split("\n") #time, distance
t_2 = int(t.split(":")[1].strip().replace(" ","")) # part 2 time
d_2 = int(d.split(":")[1].strip().replace(" ","")) # part 2 distance
t = tuple(int(x) for x in t.split(":")[1].strip().split(" ") if x)
d = tuple(int(x) for x in d.split(":")[1].strip().split(" ") if x)
races = []
for i, time in enumerate(t):
    races.append((time,d[i]))

def possible_wins(race):
    wins_n = 0
    for i in range(race[0]):        
        if i*(race[0]-i) > race[1]:
            wins_n += 1
    return wins_n

wins_mult = 1
for race in races:
    wins_mult *= possible_wins(race)
print("part 1 solution is", wins_mult)
print("part 2 solution is", possible_wins((t_2, d_2)))