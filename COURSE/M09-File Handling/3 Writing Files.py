# =========================================
# Topic : Writing Files
# =========================================

# Opening file in write mode

file = open("marks.txt", "w")

# Writing data into file
file.write("Madhav = 95\n")

file.write("Arjun = 88\n")

file.write("Karan = 91\n")

print("Data Written Successfully")

file.close()

# =========================================
# Appending data
# =========================================

file = open("marks.txt", "a")

file.write("Simran = 97\n")

print("New Data Added")

file.close()

# Reading updated file

file = open("marks.txt", "r")

print(file.read())

file.close()