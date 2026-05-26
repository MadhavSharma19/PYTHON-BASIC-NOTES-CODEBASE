# =========================================
# Topic : Abstraction
# =========================================

# Abstraction means hiding implementation
# and only showing important features

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    # Abstract method
    @abstractmethod
    def start(self):

        pass


# Child class
class Car(Vehicle):

    # Defining abstract method
    def start(self):

        print("Car Started")


# Creating object
c1 = Car()

c1.start()

# User only knows:
# Car starts
# User does not know internal engine working