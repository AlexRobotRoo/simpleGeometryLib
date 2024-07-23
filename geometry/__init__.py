# Основной __init__.py для пакета geometry
from .shapes import Shape, Circle, Triangle, Square
from .area_calculator import AreaCalculator

__all__ = ["Shape", "Circle", "Triangle", "Square", "AreaCalculator"]