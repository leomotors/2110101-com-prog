# pylint: disable=C,W,E

mname = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]


def read_date():  # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
    date = input().split()
    d = int(date[0])
    m = mname.index(date[1][:3]) + 1
    y = int(date[2])
    return [d, m, y]


def zodiac(d, m):  # คืนชื่อราศีของวัน d เดือน m
    if d >= 22 and m == 3 or d <= 21 and m == 4:
        return "Aries"
    elif d >= 22 and m == 4 or d <= 21 and m == 5:
        return "Taurus"
    elif d >= 22 and m == 5 or d <= 21 and m == 6:
        return "Gemini"
    elif d >= 22 and m == 6 or d <= 21 and m == 7:
        return "Cancer"
    elif d >= 22 and m == 7 or d <= 21 and m == 8:
        return "Leo"
    elif d >= 22 and m == 8 or d <= 21 and m == 9:
        return "Virgo"
    elif d >= 22 and m == 9 or d <= 21 and m == 10:
        return "Libra"
    elif d >= 22 and m == 10 or d <= 21 and m == 11:
        return "Scorpio"
    elif d >= 22 and m == 11 or d <= 21 and m == 12:
        return "Sagittarius"
    elif d >= 22 and m == 12 or d <= 20 and m == 1:
        return "Capricorn"
    elif d >= 21 and m == 1 or d <= 20 and m == 2:
        return "Aquarius"
    elif d >= 21 and m == 2 or d <= 21 and m == 3:
        return "Pisces"


def days_in_feb(y):  # คืนจำนวนวันของเดือนกุมภาพันธ์ในปี y
    if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
        return 29
    else:
        return 28


def days_in_month(m, y):  # คืนจำนวนวันของเดือน m ในปี y
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        return days_in_feb(y)
    else:
        return 31


def days_in_between(d1, m1, y1, d2, m2, y2):
    # คืนจำนวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2
    days = 0
    if m1 < 12:
        days += 31
    if m1 < 11:
        days += 30
    if m1 < 10:
        days += 31
    if m1 < 9:
        days += 30
    if m1 < 8:
        days += 31
    if m1 < 7:
        days += 31
    if m1 < 6:
        days += 30
    if m1 < 5:
        days += 31
    if m1 < 4:
        days += 30
    if m1 < 3:
        days += 31
    if m1 < 2:
        days += days_in_feb(y1)
    if m2 > 1:
        days += 31
    if m2 > 2:
        days += days_in_feb(y2)
    if m2 > 3:
        days += 31
    if m2 > 4:
        days += 30
    if m2 > 5:
        days += 31
    if m2 > 6:
        days += 30
    if m2 > 7:
        days += 31
    if m2 > 8:
        days += 31
    if m2 > 9:
        days += 30
    if m2 > 10:
        days += 31
    if m2 > 11:
        days += 30
    days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1) * 365.25) + (d2 - 1)
    return days


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()

    # แสดง ราศีของ d1,m1,y1 กับ ของ d2,m2,y2 บรรทัดเดียวกัน คั่นด้วยช่องว่าง\
    print(zodiac(d1, m1), zodiac(d2, m2))
    # แสดงจำนวนวันตั้งแต่ d1,m1,y1 ถึง d2,m2,y2
    print(days_in_between(d1, m1, y1, d2, m2, y2))


exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
