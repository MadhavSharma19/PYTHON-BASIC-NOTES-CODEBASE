# =========================================
# Topic : Reading Files
# =========================================

# Creating and writing file first

file = open("student.txt", "w")

file.write("Madhav\n")
file.write("Python Developer\n")
file.write("Age = 21")

file.close()

# Reading file

file = open("student.txt", "r")

# Reading complete file
data = file.read()

print(data)

file.close()

# =========================================
# Reading line by line
# =========================================

file = open("student.txt", "r")

print(file.readline())

print(file.readline())

file.close()