# =========================================
# Topic : Encapsulation
# =========================================

# Encapsulation means wrapping data
# and methods together in one class

class Bank:

    def __init__(self):

        # Private variable
        self.__balance = 50000

    # Method to access balance
    def show_balance(self):

        print("Balance =", self.__balance)

    # Method to deposit money
    def deposit(self, amount):

        self.__balance += amount

        print("Amount Deposited")

# Creating object
b1 = Bank()

# Accessing through method
b1.show_balance()

# Depositing money
b1.deposit(5000)

b1.show_balance()

# Cannot access directly
# print(b1.__balance)