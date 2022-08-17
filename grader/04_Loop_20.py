minred = 10 ** 69
maxred = -10 ** 69
minblue = 10 ** 69
maxblue = -10 ** 69

swap = False

while True:
    s = input()

    if s == "Zig-Zag":
        print(minred, maxblue)
        break

    if s == "Zag-Zig":
        print(minblue, maxred)
        break

    x, y = (int(k) for k in s.split(" "))

    if (swap):
        x, y = y, x

    minred = min(minred, x)
    maxred = max(maxred, x)
    minblue = min(minblue, y)
    maxblue = max(maxblue, y)

    swap = not swap
