from functools import reduce


class ඞඞ:
    def __init__(self, code: str):
        self.code = code

    def ඞ(self, *args):
        return int("".join(map(lambda x: self.code[x - 1], args)))


ඞඞඞ = ඞඞ(input())

ඞ๑ = ඞඞඞ.ඞ(4, 11, 18, 25, 32)
ඞ๒ = ඞඞඞ.ඞ(8, 13, 18, 23, 28)

ඞ๓ = ඞ๑ + ඞ๒ + int("๑๐๐๐๐")

ඞ๔ = (ඞ๓ // 10) % 1000

ඞ๕_s = str(ඞ๔)
ඞ๕ = reduce(lambda prev, curr: prev + int(curr), ඞ๕_s, 0) % 10 + 1

ඞ๖ = chr(ord('A') - 1 + ඞ๕)

print("{}{}".format(ඞ๔, ඞ๖))
