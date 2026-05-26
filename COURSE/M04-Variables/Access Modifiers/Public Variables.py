# =========================================
# Topic : Public Variables
# =========================================

class Student:

    def __init__(self):

        # Public variable
        self.name = "Madhav"

# Creating object
s1 = Student()

# Accessing directly
print(s1.name)

# Modifying directly
s1.name = "Arjun"

print(s1.name)