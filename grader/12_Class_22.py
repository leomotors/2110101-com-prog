class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    def getScore(self):
        if self.value == "A":
            return 1
        elif self.value in ["J", "Q", "K"]:
            return 10
        else:
            return int(self.value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    _CARD_ORDER = ["3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K", "A", "2"]
    _SUIT_ORDER = ["club", "diamond", "heart", "spade"]

    def __lt__(self, rhs):
        ms = self._CARD_ORDER.index(self.value)
        os = self._CARD_ORDER.index(rhs.value)

        if ms < os:
            return True
        elif ms > os:
            return False
        else:
            return self._SUIT_ORDER.index(
                self.suit) < self._SUIT_ORDER.index(
                rhs.suit)


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
