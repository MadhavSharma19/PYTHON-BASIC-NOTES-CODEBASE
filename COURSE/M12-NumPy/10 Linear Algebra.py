# =========================================
# Topic : Linear Algebra
# =========================================

import numpy as np

a = np.array([

    [1, 2],

    [3, 4]
])

b = np.array([

    [5, 6],

    [7, 8]
])

# Matrix multiplication
print(np.dot(a, b))

# Determinant
print(np.linalg.det(a))

# Inverse matrix
print(np.linalg.inv(a))

# Eigen values
print(np.linalg.eig(a))