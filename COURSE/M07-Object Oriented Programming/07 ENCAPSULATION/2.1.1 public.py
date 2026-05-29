# =========================================
# Topic : Encapsulation
# Subtopic : Public Access Specifier
# =========================================

# Public variables and methods
# can be accessed from anywhere

# Syntax:
# variable_name

class Student:

    # Constructor
    def __init__(self):

        # Public variable
        self.name = "Madhav"

        self.course = "Python"

    # Public method
    def show(self):

        print("Student Name =", self.name)

        print("Course =", self.course)


# Creating object
s1 = Student()

# Accessing public variables directly
print(s1.name)

print(s1.course)

# Calling public method
s1.show()

# Changing public variable
s1.name = "Arjun"

print(s1.name)

# =========================================
# Understanding
# =========================================

# Public members:
# Accessible everywhere

# Used when data does not need protection

# Real Life Example:
# College Notice Board
# Everyone can see the information