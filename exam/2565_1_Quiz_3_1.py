n = int(input())

team_to_country = {}

for i in range(n):
    team, country = input().split(" ")
    team_to_country[team] = country

def validate(teams):
    seen = set()
    for team in teams:
        if team not in team_to_country.keys():
            return False

        country = team_to_country[team]
        if country in seen:
            return False
        seen.add(country)

    return True

while True:
    token = input()

    if token == "q":
        break

    teams = token.split(" ")

    if validate(teams):
        print("OK")
    else:
        print("Not OK")
