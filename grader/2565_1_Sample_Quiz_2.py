file_path = input()
pattern = input()
replace = input()


def my_split(st, delim):
    tokens = []
    curr = ""

    for s in st:
        if s == delim:
            tokens.append(curr)
            curr = ""
        else:
            curr += s

    if curr != "":
        tokens.append(curr)

    return tokens


def my_join(tokens, delim):
    res = ""

    for i, token in enumerate(tokens):
        res += token

        if i != len(tokens) - 1:
            res += delim

    return res


def match(a: str, b: str):
    a = a.lower()
    b = b.lower()

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i] and a[i] != "?":
            return False

    return True


def transform(old: str) -> str:
    if ":" in old:
        return old

    if match(pattern, old):
        return replace

    return old


with open(file_path) as f:
    for line in f:
        tokens = my_split(line, "/")

        new_tokens = []

        for i, token in enumerate(tokens):
            new_tokens.append(
                token
                if i == len(tokens) - 1 and tokens[len(tokens) - 1] != "/" else
                transform(token))

        print(my_join(new_tokens, "/"))
