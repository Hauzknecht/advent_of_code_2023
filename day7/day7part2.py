from collections import Counter

f = open("input.txt", "r")

card_val = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 11,
    "K": 12,
    "A": 13
}

class Hand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet
        self.score = 0

        

        for i, card in enumerate(self.hand, start=1):
            self.score += (13 ** (5 - i)) * card_val[card]
        if "J" not in self.hand:
            self.score += (13**5) * self.get_tier(self.hand)
        else:
            best_tier = 0
            for card in card_val.keys():
                updated_hand = self.hand.replace("J", card)
                if self.get_tier(updated_hand)>best_tier:
                    best_tier = self.get_tier(updated_hand)
            self.score += (13**5) * best_tier

        
    def get_tier(self,hand):
            c = Counter(hand)
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
            return tier
        

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