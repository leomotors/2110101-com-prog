def getAbbrev(num: int) -> str:
    if num < 1000:
        return str(num)

    if num < 10 ** 4:
        return "{}K".format(round(num / 1000, 1))

    if num < 10 ** 6:
        return "{}K".format(round(num / 1000))

    if num < 10 ** 7:
        return "{}M".format(round(num / 10 ** 6, 1))

    if num < 10 ** 9:
        return "{}M".format(round(num / 10 ** 6))

    if num < 10 ** 10:
        return "{}B".format(round(num / 10 ** 9, 1))

    return "{}B".format(round(num / 10 ** 9))


print(getAbbrev(int(input())))
