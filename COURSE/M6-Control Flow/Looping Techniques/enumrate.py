# enumerate() - get index and value
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for idx, n in enumerate(zip(names,scores), start=1):
    print(f"{idx}. {n}")
