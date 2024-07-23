import unittest
from geometry.shapes import Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

if __name__ == '__main__':
    unittest.main()