# pylint: disable=C,W

from functools import reduce


def make_int_list(x):
    # รับสตริง x มาแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
    # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]

    filtered = x.strip()

    if (not len(filtered)):
        return []

    return list(int(k) for k in filtered.split(' '))


def is_odd(e):
    # คืนค่าจริงเมื่อ e เป็นจำนวนคี่ ถ้าไม่ใช่ คืนค่าเท็จ
    return not not e % 2


def odd_list(alist):
    # คืน list ที่มีค่าเหมือน alist แต่มีเฉพาะตัวที่เป็นจำนวนคี่
    # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
    return list(filter(is_odd, alist))


def sum_square(alist):
    # คืนผลรวมของกำลังสองของแต่ละค่าใน alist
    # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
    return reduce(lambda prev, curr: prev + curr * curr, alist, 0)


exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
