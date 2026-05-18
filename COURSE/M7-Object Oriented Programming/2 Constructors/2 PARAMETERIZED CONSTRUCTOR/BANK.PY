# =========================================
# Topic: Parameterized Constructor
# Real Life Scenario: Bank Account
# =========================================

class BankAccount:

    # Parameterized Constructor
    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    # Method
    def show_balance(self):

        print("Account Holder :", self.name)
        print("Balance :", self.balance)


# Creating Objects
user1 = BankAccount("Rahul", 50000)
user2 = BankAccount("Priya", 75000)

# Display Data
user1.show_balance()

user2.show_balance()