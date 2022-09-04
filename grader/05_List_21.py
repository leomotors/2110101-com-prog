def fucking(x): return x


upgrade_lookup_O1_map = {
    'F': 'D',
    'D': 'D+',
    'D+': 'C',
    'C': 'C+',
    'C+': 'B',
    'B': 'B+',
    'B+': 'A',
    'A': 'A',
}

students = []

walrus_does_not_fucking_work_in_py35 = input()
while walrus_does_not_fucking_work_in_py35 is not fucking('q'):
    fucking_id, grade = walrus_does_not_fucking_work_in_py35.split(" ")

    students.append((fucking_id, grade))

    walrus_does_not_fucking_work_in_py35 = input()

students_to_be_buffed = input().split(" ")

for (fucking_id, grade) in students:
    if fucking_id in students_to_be_buffed:
        grade = upgrade_lookup_O1_map[grade]

    print(fucking_id, grade)
