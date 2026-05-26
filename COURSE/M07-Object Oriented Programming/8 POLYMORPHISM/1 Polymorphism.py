# =========================================
# Topic : Polymorphism
# =========================================

# Polymorphism means:
# One thing with many forms

class Dog:

    def sound(self):

        print("Dog barks")


class Cat:

    def sound(self):

        print("Cat meows")


# Same method name
# Different behavior

d1 = Dog()

c1 = Cat()

d1.sound()

c1.sound()