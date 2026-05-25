# =========================================
# Topic : deque
# =========================================

# deque allows fast insertion and deletion

from collections import deque

# Creating deque
d = deque([10, 20, 30])

print(d)

# Adding at end
d.append(40)

print(d)

# Adding at beginning
d.appendleft(5)

print(d)

# Removing from end
d.pop()

print(d)

# Removing from beginning
d.popleft()

print(d)

# Real life example
queue = deque()

queue.append("Madhav")

queue.append("Arjun")

queue.append("Simran")

print(queue)

queue.popleft()

print(queue)