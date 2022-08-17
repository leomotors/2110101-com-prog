# pylint: disable=exec-used

def student_is_worthy_to_enter_the_quality_program(student) -> bool:
    return student[2] == 'A' and student[3] in ['A', 'B', 'C'] and student[4] in ['A', 'B', 'C']


def choose(s1, s2):
    students = list(
        filter(
            student_is_worthy_to_enter_the_quality_program,
            (s1, s2)))

    if len(students) <= 1:
        return list(map(lambda s: s[0], students))

    id0 = [students[0][0]]
    id1 = [students[1][0]]

    assert (len(students) == 2)

    if students[0][1] > students[1][1]:
        return id0
    elif students[0][1] < students[1][1]:
        return id1
    else:
        if ord(students[0][3]) < ord(students[1][3]):
            return id0
        elif ord(students[0][3]) > ord(students[1][3]):
            return id1
        else:
            if ord(students[0][4]) < ord(students[1][4]):
                return id0
            elif ord(students[0][4]) > ord(students[1][4]):
                return id1
            else:
                return list(map(lambda s: s[0], students))


exec(input())
