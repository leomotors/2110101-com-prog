from functools import cmp_to_key


points_pre = {
    1: 'AEILNORSTU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}

points = {}

for point, chars in points_pre.items():
    for c in chars:
        points[c] = point


def word_point(w):
    # คืนคะแนนของคำที่เก็บในตัวแปร w ที่หาได้จากผลรวมของคะแนนของทุกตัวอักษรใน w
    return sum(points[c] for c in w)


words = input().split()

entries = []

for word in words:
    entries.append([word, word_point(word)])


def cmp(x, y):
    if x[1] > y[1]:
        return -1
    if x[1] < y[1]:
        return 1

    if x[0] > y[0]:
        return 1
    if x[0] < y[0]:
        return -1
    return 0


entries.sort(key=cmp_to_key(cmp))

for entry in entries:
    print(entry[0], entry[1])
