# =========================================
# Topic : defaultdict
# =========================================

# defaultdict automatically creates default values

from collections import defaultdict

# Integer default value
d = defaultdict(int)

# Adding values
d["Python"] += 1

d["Python"] += 1

d["Java"] += 1

print(d)

# Accessing missing key
print(d["C++"])

# List default value
students = defaultdict(list)

students["Python"].append("Madhav")

students["Python"].append("Arjun")

students["Java"].append("Simran")

print(students)