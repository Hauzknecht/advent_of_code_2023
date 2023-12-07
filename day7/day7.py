from collections import Counter

f = open("input.txt", "r")

card_val = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

class Hand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet
        self.score = 0

        c = Counter(self.hand)
        t = sorted(c.values(), reverse=True)
        tier = 0
        if t == [5]:
            tier = 7
        if t == [4, 1]:
            tier = 6
        if t == [3, 2]:
            tier = 5
        if t == [3, 1, 1]:
            tier = 4
        if t == [2, 2, 1]:
            tier = 3
        if t == [2, 1, 1, 1]:
            tier = 2
        if t == [1, 1, 1, 1, 1]:
            tier = 1

        for i, card in enumerate(self.hand, start=1):
            self.score += (13 ** (5 - i)) * card_val[card]
        self.score += (13**5) * tier
        

    def __repr__(self) -> str:
        return f"{self.hand} {self.bet} {self.score}"

hands = []
for h in f.read().split("\n"):
    h = h.split(" ")
    cards, bet = h[0], int(h[1])
    hands.append(Hand(cards,bet))
hands.sort(key=lambda x: x.score)

total = 0
for i, hand in enumerate(hands, start=1):
    total += hand.bet*i
print("Part 1 solution is", total)