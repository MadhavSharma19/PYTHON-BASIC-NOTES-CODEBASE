# =========================================
# Topic : Protected Access Specifier
# with Inheritance
# =========================================

class Bank:

    def __init__(self):

        # Protected variable
        self._balance = 70000
        self.name="naman"


# Child class
class Customer(Bank):

    def show_balance(self):

        # Accessing protected variable
        print("Balance =", self._balance)

class faltu:
    def __init__(self):
        pass



ob=Customer()

print(ob._balance)

# =========================================
# Understanding
# =========================================

# Protected members are mainly
# designed for subclasses

# Best use:
# Parent-child relationship