# pylint: disable=W

phone_keys = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ"
}

phones = {}

for key, chars in phone_keys.items():
    for i, char in enumerate(chars.lower()):
        phones[char] = key * (i + 1)

phones[" "] = "0"

phones_reverse = ({v: k for k, v in phones.items()})


def text2keys(text):
    return " ".join(
        filter(
            lambda x: not not len(x),
            map(lambda x: phones.get(x, ""),
                text.lower())))


def keys2text(keys):
    return "".join(map(lambda x: phones_reverse.get(x, ""), keys.split(" ")))


# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
exec(input().strip())
