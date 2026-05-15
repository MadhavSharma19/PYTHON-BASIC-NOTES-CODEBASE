# =========================================
# Topic: Constructor with Default Values
# Real Life Scenario: Car Showroom
# =========================================

class Car:

    # Constructor with default values
    def __init__(self, brand="Toyota", color="Black"):

        self.brand = brand
        self.color = color

    # Method
    def show_car(self):

        print("Brand :", self.brand)
        print("Color :", self.color)


# Object with default values
car1 = Car()

# Object with custom values
car2 = Car("BMW", "White")

print("Car 1 Details")
car1.show_car()

print()

print("Car 2 Details")
car2.show_car()