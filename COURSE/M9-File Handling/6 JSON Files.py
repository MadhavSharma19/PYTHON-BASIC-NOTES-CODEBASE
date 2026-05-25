# =========================================
# Topic : JSON Files
# =========================================

# JSON = JavaScript Object Notation

import json

# Python dictionary
student = {

    "name": "Madhav",

    "age": 21,

    "course": "Python"
}

# =========================================
# Writing JSON file
# =========================================

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)

print("JSON File Created")

# =========================================
# Reading JSON file
# =========================================

with open("student.json", "r") as file:

    data = json.load(file)

    print(data)

    print(data["name"])

    print(data["course"])