# =========================================
# Topic : Local Variables
# =========================================

# Function
def demo():

    # Local variable
    marks = 95

    print("Inside Function =", marks)

# Calling function
demo()

# This will give error because
# local variable cannot be used outside
# print(marks)

# Another example
def bill():

    burger = 120

    pizza = 250

    total = burger + pizza

    print("Total Bill =", total)

bill()