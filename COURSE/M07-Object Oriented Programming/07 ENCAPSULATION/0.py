class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

 
    def __str__(self):
        return f"{self.__class__.__name__}: area = {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height



# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(shape)  # Each calls its own area() method
