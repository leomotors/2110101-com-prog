from functools import reduce

needle = input()
haystack = input()

print(
    reduce(
        lambda prev, curr: prev + (curr == needle),
        "".join(map(lambda x: " " if x in "\"'(),." else x, tuple(haystack))).split(
            " "),
        0))
