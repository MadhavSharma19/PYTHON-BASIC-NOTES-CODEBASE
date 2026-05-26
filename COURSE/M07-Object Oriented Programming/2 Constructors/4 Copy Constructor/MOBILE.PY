
# =========================================
# Topic: Copy Constructor
# Real Life Scenario: Mobile Clone
# =========================================

class Mobile:

    # Constructor
    def __init__(self, brand, price):

        self.brand = brand
        self.price = price

    # Copy Constructor
    @classmethod
    def copy_constructor(cls, other_object):

        return cls(other_object.brand, other_object.price)

    # Method
    def show_mobile(self):

        print("Brand :", self.brand)
        print("Price :", self.price)


# Original Object
mobile1 = Mobile("iPhone", 80000)

# Copy Object
mobile2 = Mobile.copy_constructor(mobile1)

print("Original Mobile")
mobile1.show_mobile()

print()

print("Copied Mobile")
mobile2.show_mobile()