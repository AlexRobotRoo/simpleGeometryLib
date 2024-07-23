import unittest
from geometry.shapes import Circle, Triangle, Square
from geometry.area_calculator import AreaCalculator

class TestAreaCalculator(unittest.TestCase):
    def test_calculate_areas(self):
        circle = Circle(5)
        triangle = Triangle(3, 4, 5)
        square = Square(4)

        calculator = AreaCalculator()
        calculator.add_shape(circle)
        calculator.add_shape(triangle)
        calculator.add_shape(square)

        areas = calculator.calculate_areas()
        self.assertAlmostEqual(areas[0], 78.53981633974483)
        self.assertAlmostEqual(areas[1], 6.0)
        self.assertAlmostEqual(areas[2], 16.0)

if __name__ == '__main__':
    unittest.main()