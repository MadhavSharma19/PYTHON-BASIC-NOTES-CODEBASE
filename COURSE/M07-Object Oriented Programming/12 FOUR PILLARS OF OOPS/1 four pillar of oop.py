# =========================================
# Topic : Four Pillars of OOP
# =========================================

# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# =========================================
# Parent Class
# =========================================

class Animal:

    # Encapsulation
    # Storing data inside class

    def __init__(self, name):

        self.name = name

    # Abstraction
    # Only showing method name
    # Actual implementation hidden

    def sound(self):

        pass


# =========================================
# Child Class : Dog
# =========================================

# Inheritance
# Dog class inherits Animal class

class Dog(Animal):

    # Polymorphism
    # Same method with different behavior

    def sound(self):

        print(self.name, "barks")


# =========================================
# Another Child Class : Cat
# =========================================

class Cat(Animal):

    # Polymorphism again

    def sound(self):

        print(self.name, "meows")


# =========================================
# Creating Objects
# =========================================

d1 = Dog("Tommy")

c1 = Cat("Kitty")


# =========================================
# Calling Methods
# =========================================

d1.sound()

c1.sound()


# =========================================
# Accessing Encapsulated Data
# =========================================

print(d1.name)

print(c1.name)


# =========================================
# Final Understanding
# =========================================

print("\n===== FOUR PILLARS =====")

print("1. Encapsulation -> self.name")

print("2. Abstraction -> sound() method")

print("3. Inheritance -> Dog(Animal)")

print("4. Polymorphism -> Different sound()")