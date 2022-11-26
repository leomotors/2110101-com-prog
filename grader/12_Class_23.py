class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    _CARD_ORDER = ["3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K", "A", "2"]
    _SUIT_ORDER = ["club", "diamond", "heart", "spade"]

    def _next(self):
        cc = self._CARD_ORDER.index(self.value)
        cs = self._SUIT_ORDER.index(self.suit)

        cs += 1
        if cs >= 4:
            cs = 0
            cc += 1

        if cc >= 13:
            cc = 0

        return (self._CARD_ORDER[cc], self._SUIT_ORDER[cs])

    def next1(self):
        return Card(*self._next())

    def next2(self):
        self.value, self.suit = self._next()


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
