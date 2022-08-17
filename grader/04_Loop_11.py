# pylint: disable=global-statement

# O(N²) brrrrrrr

encoded = ""


def cum(curr: str, count: int, rem: str) -> None:
    global encoded

    if not len(rem):
        encoded += curr + ' ' + str(count) + ' '
        return

    if curr == rem[0]:
        cum(curr, count + 1, rem[1:])
    else:
        encoded += curr + ' ' + str(count) + ' '
        cum(rem[0], 1, rem[1:])


s = input()
cum(s[0], 1, s[1:])

print(encoded)
