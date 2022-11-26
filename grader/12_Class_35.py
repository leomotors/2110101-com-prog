class roman:
    def __init__(self, r):
        self._str = r

    _VAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self._str

    def __int__(self):
        total = 0

        strlen = len(self._str)
        for i in range(strlen):
            if i < strlen - 1 and self._VAL[self._str[i]] < self._VAL[self._str[i+1]]:
                total -= self._VAL[self._str[i]]

            else:
                total += self._VAL[self._str[i]]

        return total

    _NUM = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]

    _SYM = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]

    def _to_roman(self, num):
        i = 12
        res = ""

        while num:
            div = num // self._NUM[i]
            num %= self._NUM[i]

            while div:
                res += self._SYM[i]
                div -= 1
            i -= 1

        return res

    def __add__(self, rhs):
        return roman(self._to_roman(int(self) + int(rhs)))


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
