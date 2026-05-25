# =========================================
# Topic : ChainMap
# =========================================

# ChainMap combines multiple dictionaries

from collections import ChainMap

# Dictionary 1
student = {

    "name": "Madhav",

    "age": 21
}

# Dictionary 2
course = {

    "course": "Python",

    "duration": "6 Months"
}

# Combining dictionaries
data = ChainMap(student, course)

print(data)

# Accessing values
print(data["name"])

print(data["course"])

# Viewing combined maps
print(data.maps)