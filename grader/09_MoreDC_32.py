def first_fit(L, e):  # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for l in L:
        if sum(l) + e <= 100:
            l.append(e)
            return

    L.append([e])


def best_fit(L, e):  # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    best = []
    for i, l in enumerate(L):
        if sum(l) + e <= 100:
            best.append([100 - sum(l), i])

    best.sort()
    if len(best) > 0:
        L[best[0][1]].append(e)
    else:
        L.append([e])


def partition_FF(D):  # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    L = []
    for d in D:
        first_fit(L, d)

    return L


def partition_BF(D):  # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    L = []
    for d in D:
        best_fit(L, d)

    return L


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
