# =========================================
# Topic : Array Creation
# =========================================

import numpy as np

# 1D Array
a = np.array([1, 2, 3])

print(a)

# 2D Array
b = np.array([[1, 2], [3, 4]])

print(b)

# Zeros array
print(np.zeros((2, 3)))

# Ones array
print(np.ones((3, 3)))

# Range array
print(np.arange(1, 11))

# Linearly spaced array
print(np.linspace(1, 100, 5))