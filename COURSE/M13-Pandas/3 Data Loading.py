# =========================================
# Topic : Data Loading
# =========================================

import pandas as pd

# Loading CSV file
df = pd.read_csv("students.csv")

print(df)

# Loading Excel file
# df = pd.read_excel("students.xlsx")

# Loading JSON file
# df = pd.read_json("student.json")

# First rows
print(df.head())

# Last rows
print(df.tail())

# Shape
print(df.shape)