# =========================================
# Topic : Advanced NumPy Techniques
# =========================================

import numpy as np

a = np.array([1, 2, 3, 4])

b = np.array([5, 6, 7, 8])

# Concatenation
print(np.concatenate((a, b)))

# Splitting arrays
x = np.array([1, 2, 3, 4, 5, 6])

print(np.split(x, 3))

# Unique values
y = np.array([1, 2, 2, 3, 3, 4])

print(np.unique(y))

# Sorting
z = np.array([50, 10, 30, 20])

print(np.sort(z))

# Where function
print(np.where(z > 25))

# Copy vs View
a1 = np.array([1, 2, 3])

b1 = a1.view()

c1 = a1.copy()

print(b1)

print(c1)