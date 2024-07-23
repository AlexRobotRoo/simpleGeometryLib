from .shapes import Shape

class AreaCalculator:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def calculate_areas(self):
        return [shape.area() for shape in self.shapes]