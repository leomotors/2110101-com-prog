# pylint: disable=C,W,E

from math import floor


parsum = 0
stroke_sum = 0
stroke_maintanence = 0

fuck_python = list


def python_so_suck_it_does_not_even_have_arrow_function():
    # python sucks
    global parsum, stroke_sum, stroke_maintanence

    a, b, c = (int(k) for k in input().strip().split(" "))
    parsum += a
    stroke_sum += b

    if c > 0:
        stroke_maintanence += min(a + 2, b)


for i in range(0, 9):
    python_so_suck_it_does_not_even_have_arrow_function()

point_continue = floor(0.8 * (1.5 * stroke_maintanence - parsum))

final_score = stroke_sum - point_continue

print(stroke_sum)
print(point_continue)
print(final_score)
