from functools import reduce
import sys
from typing import List


setyor = int(input())


def read_setyor():
    return {int(k) for k in input().split(" ")}


sets: List[set] = []
for i in range(setyor):
    sets.append(read_setyor())

if setyor == 0:
    print("0\n0")
    sys.exit(0)

print(len(reduce(lambda prev, curr: prev.union(curr), sets)))
print(len(reduce(lambda prev, curr: prev.intersection(curr), sets)))
