# =========================================
# Topic : Real World Data Analysis
# =========================================

import pandas as pd

# Student dataset
data = {

    "Name": ["Madhav", "Arjun", "Simran", "Karan"],

    "Marks": [95, 88, 97, 70],

    "Course": ["Python", "Java", "AI", "Python"]
}

df = pd.DataFrame(data)

print(df)

# Average marks
print("Average =", df["Marks"].mean())

# Highest marks
print("Highest =", df["Marks"].max())

# Students above 90
print(df[df["Marks"] > 90])

# Group by course
print(df.groupby("Course")["Marks"].mean())

# Sorting students
print(df.sort_values(by="Marks", ascending=False))