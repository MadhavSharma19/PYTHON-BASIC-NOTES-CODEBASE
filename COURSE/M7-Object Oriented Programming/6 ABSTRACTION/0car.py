from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):
    def __init__(self, color="black"):
        self.color = color    # Abstract classes CAN have regular attributes


    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass


    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


    # Concrete method (regular method with implementation)
    def describe(self):
        return f"I am a {self.color} {self.__class__.__name__}"


# Trying to instantiate abstract class raises TypeError
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape


# Concrete class that implements ALL abstract methods
class Circle(Shape):
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.radius = radius


    def area(self):
        return math.pi* self.radius ** 2


    def perimeter(self):
        return 2 * 3.14159 * self.radius


class bunty(Shape):
    def __init__(self, width, height, color="blue"):
        super().__init__(color)
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


# Usage
circle = Circle(5, "red")
rect = bunty(4, 6, "blue")


print(circle.describe())     # I am a red Circle
print(f"Area: {circle.area():.2f}")        # Area: 78.54
print(f"Perimeter: {circle.perimeter():.2f}")  # Perimeter: 31.42


print(rect.describe())       # I am a blue Rectangle
print(f"Area: {rect.area()}")              # Area: 24
print(f"Perimeter: {rect.perimeter()}")    # Perimeter: 20
