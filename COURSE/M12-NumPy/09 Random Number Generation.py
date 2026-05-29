# =========================================
# Topic : Random Number Generation
# =========================================

import numpy as np

# Random float
print(np.random.rand())

# Random array
print(np.random.rand(3))

# Random integers
print(np.random.randint(1, 100, 5))

# Random matrix
print(np.random.randint(1, 10, (3, 3)))

# Random choice
names = ["Madhav", "Arjun", "Simran"]

print(np.random.choice(names))