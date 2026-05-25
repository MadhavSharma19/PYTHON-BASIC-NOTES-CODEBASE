# =========================================
# Topic : DataFrame
# =========================================

# DataFrame is a table-like structure

import pandas as pd

data = {

    "Name": ["Madhav", "Arjun", "Simran"],

    "Marks": [95, 88, 97],

    "Course": ["Python", "Java", "AI"]
}

# Creating DataFrame
df = pd.DataFrame(data)

print(df)

# Accessing column
print(df["Name"])

# Accessing rows
print(df.head())

print(df.tail())

# Information
print(df.info())