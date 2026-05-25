# =========================================
# Topic : Sets
# =========================================

# Sets are unordered
# Sets do not allow duplicates

numbers = {10, 20, 30, 20, 40}

print(numbers)

# Duplicate 20 removed automatically

# Adding element
numbers.add(50)

print(numbers)

# Removing element
numbers.remove(10)

print(numbers)

# Looping through set
for i in numbers:

    print(i)

# Membership check
print(30 in numbers)

print(100 in numbers)

# Set operations
a = {1, 2, 3}

b = {3, 4, 5}

print("Union =", a | b)

print("Intersection =", a & b)