import math


class Shape:
    def compute_area(self):
        raise NotImplementedError("Метод compute_area должен быть реализован")


class Circle(Shape):
    def __init__(self, radius):
        # если радиус меньше нуля, то такого круга быть не может
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        # сортируем стороны, чтобы проверить на допустимость треугольника
        sides = sorted([a, b, c])
        # используем свойство треугольника, что сумма двух любых сторон больше третьей
        # за третью сторону берём максимальную, чтобы не делать лишних проверок
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Стороны не образуют правильный треугольник")
        self.a, self.b, self.c = a, b, c

    def compute_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        # Теорема Пифагора
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


def area_of_shape(shape: Shape):
    return shape.compute_area()
