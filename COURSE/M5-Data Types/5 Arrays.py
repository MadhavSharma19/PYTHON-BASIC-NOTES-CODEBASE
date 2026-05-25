# =========================================
# Topic : Arrays
# =========================================

# Arrays store same datatype values

from array import *

marks = array('i', [90, 85, 70, 95])

print(marks)

# Accessing elements
print(marks[0])

print(marks[2])

# Adding element
marks.append(100)

print(marks)

# Removing element
marks.remove(70)

print(marks)

# Looping through array
for i in marks:

    print(i)

# Array length
print("Total Elements =", len(marks))