# =========================================
# Topic : Boolean Indexing
# =========================================

import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Condition
x = a > 25

print(x)

# Filtering values
print(a[x])

# Direct method
print(a[a > 30])

# Even numbers
print(a[a % 2 == 0])