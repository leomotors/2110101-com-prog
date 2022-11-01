import numpy as np


def p(X):
    # X เป็นอาเรย์ขนาด n2 เก็บจ านวนโจทย์ที่ท า (คอลัมน์ 0) กับเกรดเฉลี่ย (คอลัมน์1) ของนักเรียน n คน
    # คืนอาเรย์ขนาด n ชอ่ ง เก็บความน่าจะเป็นที่นักเรียนแต่ละคนจะเรียนผ่านวิชา ค านวณจากสูตรข ้างบน
    # ใชค้ วามสามารถของ NumPy จะเขียนได ้โดยไมต่ อ้ งใชว้งวน (อย่างมาก 3 บรรทัด)
    return 1 / (1 + np.e ** -(-3.98 + 0.1 * X[:, 0] + 0.5 * X[:, 1]))


exec(input().strip())  # ตอ้ งมคี าสงั่ นี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
