# =========================================
# Topic : Data Cleaning
# =========================================

import pandas as pd

data = {

    "Name": ["Madhav", "Arjun", None],

    "Marks": [95, None, 88]
}

df = pd.DataFrame(data)

print(df)

# Checking null values
print(df.isnull())

# Counting null values
print(df.isnull().sum())

# Filling missing values
df["Marks"] = df["Marks"].fillna(0)

df["Name"] = df["Name"].fillna("Unknown")

print(df)

# Dropping null values
print(df.dropna())