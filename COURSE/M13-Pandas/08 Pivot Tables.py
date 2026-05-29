# =========================================
# Topic : Pivot Tables
# =========================================

import pandas as pd

data = {

    "Department": ["IT", "IT", "HR", "HR"],

    "Employee": ["A", "B", "C", "D"],

    "Salary": [50000, 60000, 45000, 40000]
}

df = pd.DataFrame(data)

# Pivot table
p = df.pivot_table(

    values="Salary",

    index="Department",

    aggfunc="mean"
)

print(p)