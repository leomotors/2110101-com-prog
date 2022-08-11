import math
from functools import reduce


def sqrt_n_times(x, n):
    return reduce(lambda prev, curr: math.sqrt(prev), range(n), x)


def cube_root(y):
    return reduce(lambda prev, curr: prev * sqrt_n_times(prev, 2 ** curr), range(1, 6), sqrt_n_times(y, 2))


def main():
    q = float(input())
    print(cube_root(q))


exec(input())
