from functools import cmp_to_key


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    # คืนผลการทดสอบว่า a, b และ c เป็น coprime หรือไม่
    # อ่านนิยาม coprime ที่ https://en.wikipedia.org/wiki/Coprime_integers
    return gcd(gcd(a, b), c) == 1


def primitive_Pythagorean_triples(max_len):
    # คืนลิสต์ ทภี่ ายในเกบ็ ลสิตย์ อ่ ยทมี่ สี มาชกิสามคา่ ของ a, b และ c
    # โดยที่ a  b  c  max_len
    # ลิสต์ย่อยต่าง ๆ ถูกจัดเรียงตามค่า c จากน้อยไปมาก
    # หากมีค่า c เท่ากัน ให้เรียงตามค่า a เชน่ ถา้ max_len = 65 จะได้
    # [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25],
    # [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53],
    # [11, 60, 61], [16, 63, 65], [33, 56, 65]]
    triple = []
    for i in range(2, max_len + 1):
        for j in range(i+1, max_len + 1):
            for k in range(j+1, max_len + 1):
                if i ** 2 + j ** 2 == k ** 2 and is_coprime(i, j, k):
                    triple.append([i, j, k])
    triple.sort(
        key=cmp_to_key(
            lambda x, y: 1 if x[2] > y[2] else -1 if x[2] < y[2] else 0))

    return triple


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
