# =========================================
# Topic : namedtuple
# =========================================

# namedtuple gives names to tuple values

from collections import namedtuple

# Creating namedtuple
Student = namedtuple("Student", ["name", "age", "course"])

# Creating object
s1 = Student("Madhav", 21, "Python")

# Accessing values
print(s1.name)

print(s1.age)

print(s1.course)

# Normal tuple vs namedtuple

t = ("Madhav", 21)

print(t[0])

# Easier readability with namedtuple