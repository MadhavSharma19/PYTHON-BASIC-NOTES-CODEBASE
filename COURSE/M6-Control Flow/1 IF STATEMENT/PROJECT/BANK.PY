# ==========================================
# Project: Mini Banking System
# Concepts Used:
# - if
# - if-else
# - if-elif-else
# - nested if
# ==========================================

print("===================================")
print("      WELCOME TO PYTHON BANK")
print("===================================")

# ---------------- USER DATA ----------------
correct_pin = 1234
balance = 15000
minimum_balance = 1000
salary = 45000
credit_score = 720

# ---------------- LOGIN SYSTEM ----------------
entered_pin = int(input("Enter Your 4-Digit PIN: "))

if entered_pin == correct_pin:

    print("\n✅ Login Successful")

    # ---------------- MENU ----------------
    print("\n========= MENU =========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Apply for Loan")

    choice = int(input("\nEnter Your Choice: "))

    # ---------------- CHECK BALANCE ----------------
    if choice == 1:

        print("\n💰 Your Current Balance is:", balance)

    # ---------------- DEPOSIT ----------------
    elif choice == 2:

        deposit = int(input("Enter Amount to Deposit: "))

        if deposit > 0:

            balance = balance + deposit

            print("\n✅ Deposit Successful")
            print("Updated Balance:", balance)

        else:
            print("\n❌ Invalid Deposit Amount")

    # ---------------- WITHDRAW ----------------
    elif choice == 3:

        withdraw = int(input("Enter Withdrawal Amount: "))

        # Check sufficient balance
        if balance - withdraw >= minimum_balance:

            balance = balance - withdraw

            print("\n✅ Withdrawal Successful")
            print("Withdrawn Amount:", withdraw)
            print("Remaining Balance:", balance)

        else:
            print("\n❌ Insufficient Balance")

    # ---------------- LOAN SYSTEM ----------------
    elif choice == 4:

        print("\n🏦 Loan Eligibility Check")

        # Nested if
        if salary >= 30000:

            if credit_score >= 700:

                print("✅ Loan Approved")

            else:
                print("❌ Loan Rejected")
                print("Reason: Low Credit Score")

        else:
            print("❌ Loan Rejected")
            print("Reason: Salary Too Low")

    # ---------------- INVALID CHOICE ----------------
    else:
        print("\n❌ Invalid Menu Option")

# ---------------- WRONG PIN ----------------
else:
    print("\n❌ Incorrect PIN")
    print("Access Denied")

print("\n===================================")
print(" Thank You For Using Python Bank ")
print("===================================")