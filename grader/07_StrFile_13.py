import re

fuck = input()

fuck_python = re.sub(r"[^a-zA-Z\d\s:]", " ", fuck)


def fuckSnake(fuck_python_69420: str) -> str:
    return fuck_python_69420[0].upper() + fuck_python_69420[1:].lower()


def fuckCamel(fuck_python_69420: str) -> str:
    return fuck_python_69420.lower()


words = tuple(filter(lambda shit: not not len(shit), fuck_python.split(" ")))

print("".join((fuckCamel(words[0]), *map(fuckSnake, words[1:]))))
