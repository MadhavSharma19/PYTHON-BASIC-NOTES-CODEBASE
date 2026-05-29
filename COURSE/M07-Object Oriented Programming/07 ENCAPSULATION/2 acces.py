class BankAccount:
    def __init__(self, owner,):
        self.owner = owner           # Public
        self.__balance = 0    # Private (name-mangled)


    @property
    def balance(self):
        """Getter for balance."""
        return self.__balance


    @balance.setter
    def balance(self, amount):
        """Setter with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        raise ValueError("Deposit must be positive!")


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        raise ValueError("Invalid withdrawal amount!")


account = BankAccount("Alice", 1000)
print(account.balance)        # 1000 (using property getter)
print(account.deposit(500))   # Deposited 500. New balance: 1500
print(account.withdraw(200))  # Withdrew 200. New balance: 1300
