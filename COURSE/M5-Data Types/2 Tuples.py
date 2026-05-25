# =========================================
# Topic : Tuples
# =========================================

# Tuples are ordered but immutable
# Immutable means values cannot change

colors = ("Red", "Green", "Blue")

print(colors)

# Accessing elements
print(colors[0])

print(colors[2])

# Tuple length
print("Total Colors =", len(colors))

# Looping through tuple
for i in colors:

    print(i)

# Tuple packing
student = ("Madhav", 21, "Python")

print(student)

# Tuple unpacking
name, age, course = student

print(name)

print(age)

print(course)

# This will give error
# colors[0] = "Black"