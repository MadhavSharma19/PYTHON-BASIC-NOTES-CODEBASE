# =========================================
# Topic : Shape Manipulation
# =========================================

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

# Reshape
b = a.reshape(2, 3)

print(b)

# Flatten
print(b.flatten())

# Transpose
print(b.T)

# Shape
print(b.shape)