# =========================================
# Topic : Data Manipulation
# =========================================

import pandas as pd

data = {

    "Name": ["Madhav", "Arjun", "Simran"],

    "Marks": [95, 88, 97]
}

df = pd.DataFrame(data)

print(df)

# Adding new column
df["Result"] = ["Pass", "Pass", "Pass"]

print(df)

# Updating values
df.loc[1, "Marks"] = 90

print(df)

# Sorting
print(df.sort_values(by="Marks"))

# Filtering
print(df[df["Marks"] > 90])