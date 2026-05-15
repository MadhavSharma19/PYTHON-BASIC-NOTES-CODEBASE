# Topic: Nested if
# Real Life Scenario: Loan Approval System

salary = 50000
credit_score = 750

# First condition
if salary >= 30000:

    # Second condition
    if credit_score >= 700:
        print("Loan Approved")
    else:
        print("Low Credit Score")

else:
    print("Salary Too Low")