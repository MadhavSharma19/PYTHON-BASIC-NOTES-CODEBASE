# =========================================
# Topic : Operator Overloading
# =========================================

# Operator overloading means
# changing behavior of operators

class Student:

    def __init__(self, marks):

        self.marks = marks

    # Overloading + operator
    def __add__(self, other):

        return self.marks + other.marks


# Creating objects
s1 = Student(90)

s2 = Student(85)

# Using +
print(s1 + s2)