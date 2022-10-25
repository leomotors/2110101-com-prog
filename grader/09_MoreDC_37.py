subjects_count = int(input())

subjects = {}

for i in range(subjects_count):
    tokens = input().split(" ")
    subjects[tokens[0]] = int(tokens[1])

students_count = int(input())
students = []

for i in range(students_count):
    tokens = input().split(" ")
    sid = tokens[0]
    score = float(tokens[1])
    rank = tokens[2:]
    students.append([score, sid, rank])

students.sort()
students = reversed(students)

result = []

for student in students:
    sid = student[1]
    rank = student[2]

    for r in rank:
        if subjects[r] > 0:
            subjects[r] -= 1
            result.append([sid, r])
            break

result.sort()

for res in result:
    print(res[0], res[1])
