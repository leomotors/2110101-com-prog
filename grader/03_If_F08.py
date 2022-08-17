# pylint: disable=exec-used

from datetime import datetime


def day_of_year(d, m, y):
    y -= 543

    date = datetime(y, m, d)
    diff = date - datetime(y, 1, 1)

    return diff.days + 1


exec(input())
