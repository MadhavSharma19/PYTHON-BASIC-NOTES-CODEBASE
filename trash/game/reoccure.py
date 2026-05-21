a = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3]
m = 0
r = 0
c=[]

for i in a:

    c = 0

    for j in a:

        if i == j:

            c += 1

    if c > m:
             
        m = c
        r = i

print("Most Reoccurring Element =", r)

print("Frequency =", m)      