# =========================================
# Topic : Lists
# =========================================

# Lists are ordered and mutable
# Mutable means values can change

students = ["Madhav", "Arjun", "Karan"]

print("Original List")

print(students)

# Accessing elements
print(students[0])

print(students[1])

# Changing value
students[1] = "Navraj"

print("Updated List")

print(students)

# Adding element
students.append("Simran")

print(students)

# Removing element
students.remove("Karan")

print(students)

# Looping through list
print("\nStudent Names")

for i in students:

    print(i)

# Length of list
print("Total Students =", len(students))