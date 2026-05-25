# =========================================
# Topic : Private Variables
# =========================================

class Bank:

    def __init__(self):

        # Private variable
        self.__balance = 50000

    # Function to access private variable
    def show(self):

        print("Balance =", self.__balance)

# Creating object
b1 = Bank()

# Accessing through method
b1.show()

# This will give error
# print(b1.__balance)

# Python changes name internally
print(b1._Bank__balance)