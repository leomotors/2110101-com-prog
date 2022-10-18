def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for i, x in enumerate(t):
        if e in x:
            return i
    return 69


def flatten(t):  # return a list of ints converted from list of lists of ints t
    flatted = []
    for row in t:
        for c in row:
            if c != 0:
                flatted.append(c)

    return flatted


def inversions(x):  # return the number of inversions of list x
    inv = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                inv += 1
    return inv


def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    inv = inversions(flatten(t))

    if len(t) % 2 == 1:
        return inv % 2 == 0
    else:
        return (inv + row_number(t, 0)) % 2 == 1


exec(input().strip())  # do not remove this line
