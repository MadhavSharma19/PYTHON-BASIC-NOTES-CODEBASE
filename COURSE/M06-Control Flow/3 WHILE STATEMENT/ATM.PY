# Topic: while Loop
# Real Life Scenario: ATM PIN Check

correct_pin = "1234"

pin = ""

while pin != correct_pin:

    pin = input("Enter ATM PIN: ")

    if pin != correct_pin:
        print("❌ Wrong PIN")

print("✅ Login Successful")