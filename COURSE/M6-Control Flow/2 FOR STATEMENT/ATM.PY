# Topic: for Loop
# Real Life Scenario: ATM Attempts

for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == "1234":
        print("Login Successful")
        break