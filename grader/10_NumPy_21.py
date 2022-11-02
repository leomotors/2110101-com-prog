import numpy as np


def sum_2_rows(M: np.ndarray):
    # คืนผลที่ได ้จากการรวมจ านวนในคอลัมน์เดียวกันของแถวที่ติดกันทีละคู่แถว
    # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 4, 6, 8, 10],
    # [ 4, 5, 6, 7], [20, 22, 24, 26]]
    # [ 8, 9, 10, 11],
    # [12, 13, 14, 15]]
    rows = []
    for i in range(0, M.shape[0], 2):
        rows.append(M[i] + M[i+1])
    return np.array(rows)


def sum_left_right(M: np.ndarray):
    # คนืผลทไี่ ดจ้ากการรวมจ านวนของครงึ่ ซา้ยกับครงึ่ ขวาของ M
    # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 2, 4],
    # [ 4, 5, 6, 7], [10, 12],
    # [ 8, 9, 10, 11], [18, 20],
    # [12, 13, 14, 15]] [26, 28]]
    row, col = M.shape
    mid = col // 2
    cols = []
    for i in range(0, mid):
        shit = M[:, i] + M[:, mid+i]
        cols.append(shit.reshape(row, 1))

    return np.hstack(cols)


def sum_upper_lower(M):
    # คืนผลที่ได ้จากการรวมจ านวนของครึ่งบนกับครึ่งล่างของ M
    # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 8, 10, 12, 14],
    # [ 4, 5, 6, 7], [16, 18, 20, 22]]
    # [ 8, 9, 10, 11],
    # [12, 13, 14, 15]]
    row, col = M.shape
    mid = row // 2
    rows = []
    for i in range(0, mid):
        rows.append(M[i] + M[mid+i])

    return np.vstack(rows)


def sum_4_quadrants(M):
    # คืนผลที่ได ้จากการแบ่ง M เป็น 4 จตุภาค และรวมจ านวนที่ต าแหน่งตรงกันในแต่ละจตุภาค
    # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[20, 24],
    # [ 4, 5, 6, 7], [36, 40]]
    # [ 8, 9, 10, 11],
    # [12, 13, 14, 15]]
    n = M.shape[0]
    mid = n // 2
    res = np.ndarray((mid, mid), dtype=int)
    for i in range(mid):
        for j in range(mid):
            res[i, j] = M[i, j] + M[i, mid+j] + M[mid+i, j] + M[mid+i, mid+j]

    return res


def sum_4_cells(M):
    # คืนผลที่ได ้จากการรวมจ านวนที่ติดกัน 4 ตัว ตามรูปแบบในตัวอย่างข ้างล่างนี้
    # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[10, 18],
    # [ 4, 5, 6, 7], [42, 50]]
    # [ 8, 9, 10, 11],
    # [12, 13, 14, 15]]
    n = M.shape[0]
    mid = n // 2
    res = np.ndarray((mid, mid), dtype=int)
    for i in range(mid):
        for j in range(mid):
            ox = 2 * i
            oy = 2 * j
            res[i, j] = M[ox, oy] + M[ox, oy+1] + M[ox+1, oy] + M[ox+1, oy+1]

    return res


def count_leap_years(years):
    # years เป็นอาเรย์เก็บปี พ.ศ.
    # คืนจ านวนปีใน years ที่เป็นปีอทิกสุรทิน (ปีที่ ก.พ. มี 29 วัน)
    ks = years - 543

    return np.count_nonzero((ks % 4 == 0) & (ks % 100 != 0) | (ks % 400 == 0))


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
