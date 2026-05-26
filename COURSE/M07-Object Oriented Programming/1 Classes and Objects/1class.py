class Car:
    # Class attribute (shared by all instances)
    wheels = 4


    # Constructor (initializer)
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0


    # Instance method
    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} {self.model} speed: {self.speed} km/h")


    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Braking... Speed: {self.speed} km/h")


    # String representation
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# Creating objects
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2024)


print(car1)             # 2023 Toyota Camry
car1.accelerate(60)     # Toyota Camry speed: 60 km/h
car1.accelerate(40)     # Toyota Camry speed: 100 km/h
car1.brake(30)          # Braking... Speed: 70 km/h
print(Car.wheels)       # 4 (class attribute)
