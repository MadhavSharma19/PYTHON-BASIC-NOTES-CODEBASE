# =========================================
# Topic : try-except-else-finally
# =========================================

try:

    age = int(input("Enter Your Age = "))

    print("Age Entered")

except:

    print("Invalid Input")

else:

    # Runs if no exception
    print("Welcome")

finally:

    # Always runs
    print("Program Finished")

# finally block runs
# whether exception occurs or not