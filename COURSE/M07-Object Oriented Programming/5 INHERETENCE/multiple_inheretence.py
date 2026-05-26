# Topic: Multiple Inheritance in Python

# First parent class
class Father:

    def bike(self):

        print("Father has a bike")


# Second parent class
class Mother:

    def car(self):

        print("Mother has a car")


# Child class inheriting from both classes
class Child(Father, Mother):

    def house(self):

        print("Child has a house")


# Creating object of child class
c1 = Child()

# Calling methods from Father class
c1.bike()

# Calling methods from Mother class
c1.car()

# Calling method from Child class
c1.house()