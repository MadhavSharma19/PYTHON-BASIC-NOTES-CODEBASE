# =========================================
# Topic : Dictionary
# =========================================

# Dictionary stores data in key:value pair

student = {

    "name": "Madhav",

    "age": 21,

    "course": "Python"
}

print(student)

# Accessing values
print(student["name"])

print(student["course"])

# Adding new key
student["marks"] = 95

print(student)

# Updating value
student["age"] = 22

print(student)

# Looping through dictionary
for i in student:

    print(i, "=", student[i])

# Dictionary methods
print(student.keys())

print(student.values())