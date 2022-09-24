ඞ = int

ก, ข, ค, ง = (ඞ(ฆ) for ฆ in input().split(' '))

if ก > ข:
    ก, ข = ข, ก

    while ง >= ก:
        if ค > ง:
            ก += 1
        else:
            ง -= 1

else:
    if ค % ඞ("๒") == ඞ("๐"):
        ง += ก
    else:
        if ง > ค:
            ค += ง
        else:
            ข += ก

        ก = ข + ค

print(ก, ข, ค, ง)
