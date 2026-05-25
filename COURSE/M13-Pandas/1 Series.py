# =========================================
# Topic : Pandas Series
# =========================================

# Series is a one-dimensional labeled array

import pandas as pd

# Creating Series
a = pd.Series([10, 20, 30, 40])

print(a)

# Custom index
b = pd.Series(

    [90, 85, 95],

    index=["Math", "Science", "Python"]
)

print(b)

# Accessing values
print(b["Python"])

# Series properties
print(a.size)

print(a.dtype)