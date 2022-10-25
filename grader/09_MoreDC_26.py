persons = int(input())

people = {}
fuck_python = []

for i in range(persons):
    uid, rest = input().split(":")
    items = set(rest.strip().split(", "))

    people[uid] = items
    fuck_python.append(uid)

target = input()

target_items = people[target]

found = False
for person in fuck_python:
    if person == target:
        continue

    if len(people[person].intersection(target_items)) > 0:
        print(person)
        found = True

if not found:
    print("Not Found")
