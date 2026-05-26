# ── Single Inheritance Example ──


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


    def speak(self):
        return f"{self.name} says {self.sound}"


    def info(self):
        return f"I am {self.name}"


# Dog inherits from Animal (single inheritance)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Call parent constructor
        self.breed = breed              # Add new attribute


    def fetch(self):                    # Add new method
        return f"{self.name} fetches the ball!"


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())   # Buddy says Woof (inherited method)
print(dog.info())    # I am Buddy (inherited method)
print(dog.fetch())   # Buddy fetches the ball! (own method)
print(dog.breed)     # Golden Retriever (own attribute)
