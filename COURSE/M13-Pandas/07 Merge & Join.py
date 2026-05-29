# =========================================
# Topic : Merge & Join
# =========================================

import pandas as pd

# First DataFrame
a = pd.DataFrame({

    "ID": [1, 2, 3],

    "Name": ["Madhav", "Arjun", "Simran"]
})

# Second DataFrame
b = pd.DataFrame({

    "ID": [1, 2, 3],

    "Marks": [95, 88, 97]
})

# Merging
c = pd.merge(a, b, on="ID")

print(c)