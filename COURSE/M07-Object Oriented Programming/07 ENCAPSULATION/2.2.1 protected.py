# =========================================
# Topic : Encapsulation
# Subtopic : Protected Access Specifier
# =========================================

# Protected members use:
# _variable

# Protected members should only
# be used inside class and subclass

class Teacher:

    def __init__(self):

        # Protected variable
        self._salary = 50000

    # Protected method
    def _show_salary(self):

        print("Salary =", self._salary)


# Creating object
t1 = Teacher()

# Accessing protected member
print(t1._salary)

# Calling protected method
t1._show_salary()

# =========================================
# Understanding
# =========================================

# Python does not strictly restrict access

# _variable means:
# "Please do not access directly"

# It is a naming convention

# Real Life Example:
# Staff Room
# Students should not enter,
# but technically door is not locked