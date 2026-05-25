# =========================================
# Topic : Broadcasting
# =========================================

import numpy as np

a = np.array([1, 2, 3])

# Adding scalar
print(a + 10)

# Multiplying scalar
print(a * 5)

# Broadcasting with arrays
b = np.array([10, 20, 30])

print(a + b)

# 2D Example
c = np.array([

    [1, 2, 3],

    [4, 5, 6]
])

print(c + 100)