n, m, k = (int(k) for k in input().strip().split(" "))

bandit_to_faculty = {}

for i in range(n):
    bandit, faculty = input().strip().split(" ")
    bandit_to_faculty[bandit] = faculty

guest_to_faculty = {}

for i in range(m):
    tokens = input().strip().split(" ")
    guest = tokens[0]
    visits = tokens[1:]

    visits_set = set()
    for bandit in visits:
        visits_set.add(bandit_to_faculty[bandit])

    guest_to_faculty[guest] = visits_set

for i in range(k):
    guests = input().strip().split(" ")

    guest_visit: set = guest_to_faculty[guests[0]]
    for guest in guests[1:]:
        guest_visit = guest_visit.intersection(guest_to_faculty[guest])

    if not len(guest_visit):
        print("None")
    else:
        print(" ".join(sorted(list(guest_visit))))
