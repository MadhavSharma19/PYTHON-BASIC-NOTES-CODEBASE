# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


    def start(self):
        return f"{self.brand} vehicle started"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


    def drive(self):
        return f"Driving {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


    def charge(self):
        return f"Charging {self.brand} {self.model} ({self.battery_capacity} kWh)"


# Usage
tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())    # Tesla vehicle started (from Vehicle)
print(tesla.drive())    # Driving Tesla Model 3 (from Car)
print(tesla.charge())   # Charging Tesla Model 3 (75 kWh) (from ElectricCar)
