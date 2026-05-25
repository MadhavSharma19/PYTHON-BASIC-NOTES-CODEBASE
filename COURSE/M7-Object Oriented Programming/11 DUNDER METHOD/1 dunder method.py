# =========================================
# Topic : Dunder Methods
# =========================================

# Dunder means:
# Double underscore methods

class Demo:

    # Constructor dunder method
    def __init__(self, name):

        self.name = name

    # String representation
    def __str__(self):

        return f"Student Name = {self.name}"


# Creating object
d1 = Demo("Madhav")

# Automatically calls __str__
print(d1)