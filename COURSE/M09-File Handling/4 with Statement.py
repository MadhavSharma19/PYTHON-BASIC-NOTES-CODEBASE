# =========================================
# Topic : with Statement
# =========================================

# with automatically closes file

with open("demo.txt", "w") as file:

    file.write("Python File Handling\n")

    file.write("with statement is easy")

print("File Closed Automatically")

# Reading file

with open("demo.txt", "r") as file:

    data = file.read()

    print(data)

# No need to use file.close()