# =========================================
# Topic : User Defined Exceptions
# =========================================

# Creating custom exception

class LowBalanceError(Exception):

    pass


# Bank class
class Bank:

    def __init__(self, balance):

        self.balance = balance

    def withdraw(self, amount):

        try:

            if amount > self.balance:

                raise LowBalanceError("Insufficient Balance")

            self.balance -= amount

            print("Withdrawal Successful")

            print("Remaining Balance =", self.balance)

        except LowBalanceError as e:

            print(e)


# Creating object
b1 = Bank(5000)

# Calling method
b1.withdraw(2000)

b1.withdraw(7000)