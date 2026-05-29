# =========================================
# Topic : Fancy Indexing
# =========================================

import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Accessing multiple indexes
print(a[[0, 2, 4]])

# 2D Example
b = np.array([

    [1, 2],

    [3, 4],

    [5, 6]
])

print(b[[0, 2]])