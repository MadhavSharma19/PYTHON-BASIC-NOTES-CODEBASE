# =========================================
# Project: ATM Withdrawal System
# Concept Used: if Statement
# =========================================

# User account balance
balance = 10000

# Minimum balance required
minimum_balance = 1000

# Amount user wants to withdraw
withdraw_amount = 3000

print("===== ATM MACHINE =====")
print("Current Balance:", balance)

# Check if withdrawal is possible
if balance - withdraw_amount >= minimum_balance:

    print("\nWithdrawal Approved")

    # Deduct money
    balance = balance - withdraw_amount

    print("Withdrawn Amount:", withdraw_amount)
    print("Remaining Balance:", balance)

# Message always shown
print("\nThank You For Using Our ATM")