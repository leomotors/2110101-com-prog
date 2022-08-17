# pylint: disable=exec-used

from datetime import datetime


def day_of_year(d, m, y):
    y -= 543

    diff = datetime(y, m, d) - datetime(y, 1, 1)

    return diff.days + 1


exec(input())
