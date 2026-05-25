# =========================================
# Topic : Counter
# =========================================

# Counter counts frequency of elements

from collections import Counter

# List
data = ["Python", "Java", "Python", "C++", "Python", "Java"]

# Counting elements
c = Counter(data)

print(c)

# Frequency of specific element
print("Python Count =", c["Python"])

print("Java Count =", c["Java"])

# Most common element
print(c.most_common(1))

# Real life example
text = "banana"

letters = Counter(text)

print(letters)