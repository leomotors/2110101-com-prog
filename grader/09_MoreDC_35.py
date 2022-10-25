peeps = int(input())

people = {}

for i in range(peeps):
    tokens = input().split(" ")
    people[tokens[0]] = tokens[1:]

search_term = input().split(" ")

matches = []

for peep in people.keys():
    data = people[peep]

    match = True
    for s in search_term:
        if s not in data:
            match = False
            break

    if match:
        matches.append(peep)

matches.sort()

for match in matches:
    print(match, " ".join(people[match]))

if len(matches) == 0:
    print("Not Found")
