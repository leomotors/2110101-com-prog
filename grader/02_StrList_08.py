import math


a, b, c = input().split(",")


def toDec(x, y):
    ix = int(x) if len(x) else 0
    iy = int(y) if len(y) else 0

    if y == "0":
        return [ix, 10 ** len(x)]

    if x == "":
        return [iy, 10 ** len(y) - 1]

    return [int(x + y) - int(x), int("9" * len(y) + "0" * len(x))]


d, n = toDec(b, c)

gcd = math.gcd(d, n)

d //= gcd
n //= gcd

if d == 0:
    n = 1

print("{} / {}".format(d + int(a) * n, n))
