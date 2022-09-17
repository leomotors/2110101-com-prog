# pylint: disable=C,W

from functools import reduce
import math


def distance1(x1, y1, x2, y2):
    # คืนระยะห่างระหว่างจุด (x1,y1) กับ (x2,y2)
    # ตัวอย่างการใช้: d1 = distance1(0.0, 0, 3, 4) ได้ d1 = 5.0
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def distance2(p1, p2):
    # p1 และ p2 เป็นลิสต์
    # แต่ละลิสต์แทนจุด ที่เป็นลิสต์ที่ภายในมี 2 ช่อง เก็บพิกัด x กับ y
    # คืนระยะระหว่างจุด p1 กับ p2
    # ตัวอย่างการใช้: d2 = distance2([0.0, 0], [3, 4]) ได้ d2 = 5.0
    return distance1(p1[0], p1[1], p2[0], p2[1])


def distance3(c1, c2):
    # c1 และ c2 แทนวงกลม 2 วง
    # แต่ละลิสต์เป็นลิสต์ 3 ช่อง เก็บพิกัด x กับ y (ของจุดศูนย์กลาง) และรัศมี
    # คืนระยะระหว่างจุดศูนย์กลางของ c1 กับ c2 และค่าจริง/เท็จว่า c1 กับ c2 แตะหรือทับกันหรือไม่
    # ตัวอย่างการใช้: d3,overlap = distance3([0.0, 0, 1], [5, 0, 2])
    # ได้ d3 = 5.0, overlap = False
    d = distance2(c1, c2)
    return (d, d <= c1[2] + c2[2])


def perimeter(points):
    # points เป็นลิสต์ของจุดต่าง ๆ แต่ละจุดเป็นลิสต์ 2 ช่อง (เก็บพิกัด x และ y)
    # จุดเหล่านี้คือลำดับของมุมของรูปหลายเหลี่ยม (รูป k เหลี่ยมก็มี k จุด, k>=3)
    # คืนความยาวรอบรูปของรูปหลายเหลี่ยมที่กำหนดโดย points
    return reduce(lambda prev, curr: prev +
                  distance2(points[curr],
                            points[curr + 1]),
                  range(len(points) - 1),
                  0) + distance2(points[0],
                                 points[-1])


exec(input().strip())
