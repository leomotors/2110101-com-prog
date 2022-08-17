# Binary Search on 10 ** L
# Find L s.t. a = 10 ** L
# L = log_10(a)

a = float(input())


def bin_search(l: float, r: float) -> float:
    mid = (l + r) / 2

    if l > r:
        return mid

    tentomid = 10 ** mid

    if abs(tentomid - a) < 1e-9:
        return mid

    if tentomid > a:
        return bin_search(l, mid - 1e-8)
    else:
        return bin_search(mid + 1e-8, r)


print(abs(round(bin_search(0, a), 6)))
