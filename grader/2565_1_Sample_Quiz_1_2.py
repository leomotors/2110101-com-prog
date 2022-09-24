ก = int(input())
ข = int(input())
ค = int(input())

if ก < 100:
    while ข < ค:
        ก += ข**2 + ค**2
        if (ก % 10) == 5:
            break

        if ก % 2 == 0:
            ข += 1
        else:
            ค -= 1

        if (ก / (ข * ค)) > 20:
            break

else:
    if ก < ข:
        if ข < ค:
            ก = ก + 3
            ข = ก + ค
            ค = ข + ก
        else:
            if ก < ค:
                ก = 2 * ก
                ข = ก + ข
                ค = ข + ค
            else:
                ก = ค + ก
                ข = 2 * ข
                ค = ข - ก
    else:
        if ค > ก:
            ก = 3 * ข
            ข = ค + ก
            ค = ก + ข
        else:
            if ข > ค:
                ก = ข + ค
                ข = 7 * ก
                ค = ข - ก
            else:
                ก = ค - 5
                ข = ก - ข
                ค = 3 * ข

print(ก, ข, ค)
