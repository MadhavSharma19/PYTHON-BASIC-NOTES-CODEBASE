# =========================================
# Topic : Built-in Exceptions
# =========================================

# =========================================
# ZeroDivisionError
# =========================================

try:

    print(10 / 0)

except ZeroDivisionError:

    print("Cannot divide by zero")

# =========================================
# ValueError
# =========================================

try:

    age = int(input("Enter Age = "))

except ValueError:

    print("Only numbers allowed")

# =========================================
# IndexError
# =========================================

try:

    a = [10, 20, 30]

    print(a[10])

except IndexError:

    print("Index does not exist")

# =========================================
# KeyError
# =========================================

try:

    student = {

        "name": "Madhav"
    }

    print(student["marks"])

except KeyError:

    print("Key not found")