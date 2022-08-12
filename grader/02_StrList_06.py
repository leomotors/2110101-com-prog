# pylint: disable=exec-used

def add_vector(u, v):
    return [x + y for (x, y) in zip(u, v)]


def add_vector_with_print(u, v):
    u = list(map(float, u))
    v = list(map(float, v))

    print("{} + {} = {}".format(u, v, add_vector(u, v)))


vector_u = input()
vector_v = input()

exec("add_vector_with_print({}, {})".format(vector_u, vector_v))
