# Map Country to its alliance including themself
alliances = {}


def create_alliance(countries):
    for country in countries:
        alliances[country] = countries


# Map Country to its direct enemy
enemies = {}


def _create_enemy(c1, c2):
    enemies[c1] = enemies.get(c1, set())
    enemies[c1] = enemies[c1].union({c2})


def create_enemy(countries):
    _create_enemy(countries[0], countries[1])
    _create_enemy(countries[1], countries[0])

# Check if c1 and c2 is okay to sit


def is_okay(c1, c2):
    # Is alliance of enemy
    for enemy in enemies.get(c1, set()):
        if c2 in alliances.get(enemy, [enemy]):
            return False

    # Is enemy of alliance
    for alliance in alliances.get(c1, [c1]):
        for alliances_enemy in enemies.get(alliance, set()):
            if c2 in alliances.get(alliances_enemy, [alliances_enemy]):
                return False

    return True


def _table(countries):
    for i in range(len(countries) - 1):
        if not is_okay(countries[i], countries[i + 1]):
            return False

        if not is_okay(countries[i + 1], countries[i]):
            return False

    if not is_okay(countries[0], countries[-1]):
        return False

    if not is_okay(countries[-1], countries[0]):
        return False

    return True


def table(countries):
    if _table(countries):
        print("Okay")
    else:
        print("No")


while True:
    tokens = input().strip().split(" ")
    command = tokens[0]

    if command == "Ally":
        create_alliance(tokens[1:])
    elif command == "Enemy":
        create_enemy(tokens[1:])
    elif command == "Table":
        table(tokens[1:])
    else:
        break
