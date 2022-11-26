class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"


class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2

    def area(self):
        x1, y1 = self.lowerleft.x, self.lowerleft.y
        x2, y2 = self.upperright.x, self.upperright.y

        return (x2-x1)*(y2-y1)

    def contains(self, p):
        x1, y1 = self.lowerleft.x, self.lowerleft.y
        x2, y2 = self.upperright.x, self.upperright.y
        x, y = p.x, p.y

        return x1 <= x <= x2 and y1 <= y <= y2


x1, y1, x2, y2 = [int(e) for e in input().split()]
lowerleft = Point(x1, y1)
upperright = Point(x2, y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x, y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))
