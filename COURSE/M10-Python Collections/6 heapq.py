# =========================================
# Topic : heapq
# =========================================

# heapq creates min heap

import heapq

# List
numbers = [40, 10, 30, 20, 50]

# Converting into heap
heapq.heapify(numbers)

print(numbers)

# Smallest element
print("Smallest =", numbers[0])

# Adding element
heapq.heappush(numbers, 5)

print(numbers)

# Removing smallest element
x = heapq.heappop(numbers)

print("Removed =", x)

print(numbers)

# Largest elements
print(heapq.nlargest(2, numbers))

# Smallest elements
print(heapq.nsmallest(2, numbers))