# =========================================
# Topic : Indexing & Slicing
# =========================================

import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Indexing
print(a[0])

print(a[3])

# Negative indexing
print(a[-1])

# Slicing
print(a[1:4])

print(a[:3])

print(a[2:])

# 2D Array
b = np.array([

    [1, 2, 3],

    [4, 5, 6]
])

print(b[0, 1])

print(b[1, 2])