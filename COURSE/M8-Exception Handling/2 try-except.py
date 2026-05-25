# =========================================
# Topic : try-except
# =========================================

# try:
# Code that may create exception

# except:
# Handles the exception

try:

    num1 = int(input("Enter Number 1 = "))

    num2 = int(input("Enter Number 2 = "))

    result = num1 / num2

    print("Result =", result)

except:

    print("Cannot divide by zero")

print("Program Continues")

# If exception happens,
# program will not crash