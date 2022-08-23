from datetime import datetime
import math


def fake_science_shit_formula(divider: int):
    return lambda t: math.sin(2 * math.pi * t / divider)


bd, bm, by, d, m, y = [int(e) for e in input().split()]

y -= 543
by -= 543

birthdate = datetime(by, bm, bd)
today = datetime(y, m, d)

endred = datetime(by, 12, 31)
startblue = datetime(y, 1, 1)

days_diff = (
    endred - birthdate).days + 365 * (y - by - 1) + (today - startblue).days + 1

print(
    "{} {:.2f} {:.2f} {:.2f}".format(
        days_diff, fake_science_shit_formula(23)(days_diff),
        fake_science_shit_formula(28)(days_diff),
        fake_science_shit_formula(33)(days_diff)))
