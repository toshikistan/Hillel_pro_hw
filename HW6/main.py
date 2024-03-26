# 1. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).

# Triangle - треба створити клас

import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0

    def contains(self):
        return False


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi*self.radius**2

    def __contains__(self, point):  # Обновил чтобы работало через in
        distance_to_center = (point.x - self.x)**2 + \
            (point.y - self.y)**2
        return distance_to_center <= self.radius**2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width*self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):  # Добавил площадь параллелограмма
        return self.width*self.height*math.sin(self.angle)


class Triange(Shape):  # Добавил класс треугольник и его площадь

    def __init__(self, x, y, side_a, side_b, side_c):
        super().__init__(x, y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def square(self):
        perimeter = (self.side_a + self.side_b + self.side_c)
        return math.sqrt(perimeter*(perimeter-self.side_a)*(perimeter-self.side_b)*(perimeter-self.side_c))


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)


c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)
c2 = Circle(2, 3, 5)


p = Parallelogram(1, 2, 20, 30, 45)
p1 = Parallelogram(1, 2, 20, 35, 45)
str(p1)

t = Triange(0, 0, 3, 4, 5)
t1 = Triange(1, 2, 6, 7, 10)
t2 = Triange(0, 0, 10, 11, 17)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)


print(scene.total_square())

print(p.square())
print(p1.square())
print(t.square())
print(t1.square())
print(t2.square())


# 2. 5.1 реалізувати через in.

# Point(1, 2) in Circle(1, 2, 10) -> True or False
# p1 in c1 -> True or False

p1 = Point(3, 4)
p2 = Point(5, 3)
p3 = Point(12, 7)
p4 = Point(1, 2)
p5 = Point(-2, -1)
p6 = Point(2, 7)

print(p1 in c2)
print(p2 in c2)
print(p3 in c2)
print(p4 in c2)
print(p5 in c2)
print(p6 in c2)
