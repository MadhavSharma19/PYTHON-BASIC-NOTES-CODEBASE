# Topic: Nested if
# Real Life Scenario: Login Authentication

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")