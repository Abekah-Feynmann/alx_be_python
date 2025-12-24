import math
class Shape:
    def area(self):
        raise NotImplementedError("derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = math.pi * self.radius**2
        return area

r = Rectangle(10, 3)
print(r.area())

c = Circle(7)
print(c.area())