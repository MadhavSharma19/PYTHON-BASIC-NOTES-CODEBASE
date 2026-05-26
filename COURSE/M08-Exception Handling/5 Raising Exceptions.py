# =========================================
# Topic : Raising Exceptions
# =========================================

# raise keyword is used
# to create exceptions manually

age = int(input("Enter Age = "))

try:

    if age < 18:

        raise Exception("You are not eligible")

    print("You can vote")

except Exception as e:

    print(e)

# Real life use:
# Validation systems
# Login systems
# Banking systems