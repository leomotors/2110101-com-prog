def spiral_square(n):  # n is a positive odd number
    bruh = [[0 for i in range(n)] for i in range(n)]

    center = n // 2
    x = n // 2
    y = n // 2
    radii = 0
    current = 1

    bruh[x][y] = 1

    direction = "right"

    for _ in range(n * n - 1):
        if direction == "right":
            y += 1
        if direction == "left":
            y -= 1
        if direction == "up":
            x -= 1
        if direction == "down":
            x += 1

        current += 1

        bruh[x][y] = current

        if direction == "right" and y - center > radii:
            radii += 1
            direction = "up"
        elif direction == "up" and center - x >= radii:
            direction = "left"
        elif direction == "left" and center - y >= radii:
            direction = "down"
        elif direction == "down" and x - center >= radii:
            direction = "right"

    return bruh


def print_square(S):
    # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
