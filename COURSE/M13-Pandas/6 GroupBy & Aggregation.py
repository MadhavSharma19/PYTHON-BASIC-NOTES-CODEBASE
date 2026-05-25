# =========================================
# Topic : GroupBy & Aggregation
# =========================================

import pandas as pd

data = {

    "Department": ["IT", "IT", "HR", "HR"],

    "Salary": [50000, 60000, 45000, 40000]
}

df = pd.DataFrame(data)

print(df)

# Grouping data
g = df.groupby("Department")

# Mean salary
print(g["Salary"].mean())

# Maximum salary
print(g["Salary"].max())

# Sum
print(g["Salary"].sum())