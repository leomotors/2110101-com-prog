# pylint: disable=exec-used

from typing import Dict


def total(pocket: Dict):
    return sum(k * v for k, v in pocket.items())


def take(pocket: Dict, money_in: Dict):
    for k, v in money_in.items():
        if k in pocket:
            pocket[k] += v
        else:
            pocket[k] = v


def pay(pocket: Dict, amt: int):
    keys = reversed(sorted(pocket.keys()))

    clone = pocket.copy()
    paid = {}

    for k in keys:
        while amt >= k and clone[k] > 0:
            clone[k] -= 1
            paid[k] = paid.get(k, 0) + 1
            amt -= k

    if amt != 0:
        return {}

    for k, v in clone.items():
        pocket[k] = v
    return paid


exec(input().strip())
