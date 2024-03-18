# 1. Створити клас Circle(x,y,radius). Додати метод contains.
#  Цей метод приймає екземпляр класу Point(x,y). Цей метод має повертати
#  True or False. Якшо точка в колі то True якшо поза колом то False.

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle():
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def contains(self, point):
        distance_to_center = (point.x - self.center.x)**2 + \
            (point.y - self.center.y)**2
        return distance_to_center <= self.radius**2


circle = Circle(2, 3, 5)
point1 = Point(3, 4)  # true
point2 = Point(5, 3)  # true
point3 = Point(12, 7)  # false
point4 = Point(1, 2)  # true
point5 = Point(-2, -1)  # false
point6 = Point(2, 7)  # true

print(circle.contains(point1))
print(circle.contains(point2))
print(circle.contains(point3))
print(circle.contains(point4))
print(circle.contains(point5))
print(circle.contains(point6))
