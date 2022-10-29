colors_file = input()
lyrics_file = input()

colors = []
with open(colors_file) as f:
    for l in f:
        for token in l.split(" "):
            colors.append(token.lower().strip())

colors = list(filter(lambda x: len(x) > 0, colors))


def solve(l: str):
    shadow_mistress_yuuko = l.lower()

    to_substitute = []

    for color in colors:
        loc = shadow_mistress_yuuko.find(color)

        while loc >= 0:
            to_substitute.append([loc, color])
            pos = shadow_mistress_yuuko[loc+1:].find(color)
            if pos < 0:
                break
            loc = pos + loc + 1

    to_substitute.sort()

    if len(to_substitute) == 0:
        return l

    built = l[:to_substitute[0][0]]

    for i, [loc, color] in enumerate(to_substitute):
        built += "<{}>{}</>".format(color,
                                    l
                                    [loc: loc + len(color)])

        if i < len(to_substitute) - 1:
            built += l[loc+len(color):to_substitute[i+1][0]]
        else:
            built += l[loc+len(color):]

    return built


with open(lyrics_file) as f:
    for l in f:
        print(solve(l.strip()).strip())
