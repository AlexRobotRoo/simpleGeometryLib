import math

class Shape:
    def area(self):
        raise NotImplementedError("Данный класс должен иметь подклассы!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def _validate_triangle(self):
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise ValueError("Предоставленные отрезки не образуют треугольник")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2