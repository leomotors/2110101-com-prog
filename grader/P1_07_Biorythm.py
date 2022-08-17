from datetime import datetime
from math import sin

bd, bm, by, d, m, y = [int(e) for e in input().split()]

birthdate = datetime(by, bm, bd)
date = datetime(y, m, d)

days_diff = (date - birthdate).days + 1

# IN PROGRESS
