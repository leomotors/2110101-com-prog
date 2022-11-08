token = []

voter_推し = {}
member_score = {}
member_voters = {}


def print_top_three(bruh):
    bruh.sort()
    bruh.reverse()
    print("{}, {}, {}".format(bruh[0][1], bruh[1][1], bruh[2][1]))


def rank_by_score():
    bruh = []
    for member, score in member_score.items():
        bruh.append([score, member])

    print_top_three(bruh)


def rank_by_ota_uniq():
    bruh = []

    for member, voters in member_voters.items():
        voters_count = len(voters)
        bruh.append([voters_count, member])

    print_top_three(bruh)


def rank_by_kamioshi():
    member_kamioshi = {}

    for voter, oshis in voter_推し.items():
        kamioshi = None
        kami_score = 0
        for oshi, score in oshis.items():
            if score > kami_score:
                kamioshi = oshi
                kami_score = score
            elif score == kami_score:
                if oshi < kamioshi:
                    kamioshi = oshi

        if kamioshi is not None:
            member_kamioshi[kamioshi] = member_kamioshi.get(kamioshi, 0)
            member_kamioshi[kamioshi] += 1

    for member in member_score.keys():
        if member not in member_kamioshi:
            member_kamioshi[member] = 0

    bruh = []
    for member, kamioshi in member_kamioshi.items():
        bruh.append([kamioshi, member])

    print_top_three(bruh)


while len(token) != 1:
    token = input().split(" ")

    if len(token) == 1:
        if token[0] == "1":
            rank_by_score()
        elif token[0] == "2":
            rank_by_ota_uniq()
        elif token[0] == "3":
            rank_by_kamioshi()
        break

    voter, member, score = token

    member_score[member] = member_score.get(member, 0)
    member_score[member] += int(score)

    member_voters[member] = member_voters.get(member, set())
    member_voters[member].add(voter)

    voter_推し[voter] = voter_推し.get(voter, {})
    voter_推し[voter][member] = voter_推し[voter].get(member, 0)
    voter_推し[voter][member] += int(score)
