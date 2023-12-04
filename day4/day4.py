f = open("input.txt", "r").readlines()

s = 0
cards = [1 for _ in f] # 1 card of each number

for index, line in enumerate(f):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))

    if n > 0:
        s += 2**(n-1)

    for i in range(n):
        cards[index+i+1] += cards[index] # part 2 adding copies of cards

print(s, sum(cards))