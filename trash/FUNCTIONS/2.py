# zip() - iterate over multiple sequences in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    
    print(f"{name}: {score}")


# enumerate() - get index and value
for idx, name in enumerate(names, start=1):
    print(f"{idx}. {name}")


# reversed() - iterate in reverse
for name in reversed(names):
    print(name)


# sorted() - iterate in sorted order
unsorted = [3, 1, 4, 1, 5, 9]
for num in sorted(unsorted):
    print(num, end=" ")
print()


# Using else with loops
for i in range(5):
    if i == 10:  # Never true
        break
else:
    print("Loop completed without break")

