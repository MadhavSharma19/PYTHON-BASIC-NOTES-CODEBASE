# =========================================
# Topic : Optimization
# =========================================

import pandas as pd

# Large data optimization

data = {

    "ID": [1, 2, 3, 4],

    "Marks": [90, 85, 95, 88]
}

df = pd.DataFrame(data)

print(df.info())

# Changing datatype
df["Marks"] = df["Marks"].astype("int32")

print(df.info())

# Memory usage
print(df.memory_usage())