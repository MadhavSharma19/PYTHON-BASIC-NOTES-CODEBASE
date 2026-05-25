# =========================================
# Topic : Protected Variables
# =========================================

class Student:

    def __init__(self):

        # Protected variable
        self._marks = 95

# Creating object
s1 = Student()

# Accessing protected variable
print(s1._marks)

# Protected variables use single underscore
# It means:
# "Use carefully"