n = int(input())

store = {}

people = set()

for i in range(n):
    tokens = input().split(" ")

    if tokens[0] == "B":
        person, item, price = tokens[1:]
        people.add(person)
        store[item] = store.get(item, {})
        store[item][person] = int(price) * 10 ** 69 + n - i

    if tokens[0] == "W":
        person, item = tokens[1:]

        if person in store[item]:
            store[item].pop(person)

pocket = {}
money = {}


def max_key(dic: dict):
    max_value = -1
    key = None

    for person, price in dic.items():
        if price > max_value:
            key = person
            max_value = price

    return key


for item, result in store.items():
    winner = max_key(result)

    if winner is None:
        continue

    with_price = result[winner] // 10 ** 69

    pocket[winner] = pocket.get(winner, [])
    pocket[winner].append(item)
    money[winner] = money.get(winner, 0)
    money[winner] += with_price

bruh_python_dont_have_ordered_set = sorted(people)

for person in bruh_python_dont_have_ordered_set:
    print("{}: ${}".format(person, money.get(person, 0)), end='')

    if person in pocket and len(pocket[person]) > 0:
        print(" -> {}".format(" ".join(sorted(pocket[person]))), end='')

    print()
