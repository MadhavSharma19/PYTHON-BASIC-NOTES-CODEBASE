

import math


# Parent class
class Shape:
    def __init__(self, name):
        self.name = name


    def display(self):
        print(f"Shape: {self.name}")


    def area(self):
        pass  # To be implemented by child classes




# Child class 1
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2




# Child class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width




# Child class 3
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height




# All three inherit from Shape but have unique implementations
c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(8, 6)


c.display()   # Shape: Circle    (inherited method)
r.display()   # Shape: Rectangle (inherited method)
t.display()   # Shape: Triangle  (inherited method)


print(f"Circle area: {c.area():.2f}")      # 153.94
print(f"Rectangle area: {r.area():.2f}")   # 50.00
print(f"Triangle area: {t.area():.2f}")    # 24.00
