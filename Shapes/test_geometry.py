import unittest
import math
from geometry import Circle, Triangle, area_of_shape


class ShapesTestSuite(unittest.TestCase):
    # тест на площадь круга
    def test_circle_area(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.compute_area(), expected_area, places=5)

    # тест на площадь треугольника
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.compute_area(), expected_area, places=5)

    # тест на невалидный треугольник
    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    # тест на невалидный круг, отрицательный радиус
    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    # тест на невалидный круг, нулевой радиус
    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)

    # тест на прямоугольный треугольник
    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())


    # тест на вычисление площади фигуры без знания типа фигуры в compile-time
    def test_area_of_shape_function(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(area_of_shape(circle), math.pi * 25, places=5)
        self.assertAlmostEqual(area_of_shape(triangle), 6.0, places=5)


if __name__ == '__main__':
    unittest.main()
