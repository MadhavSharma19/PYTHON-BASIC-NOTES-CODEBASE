# =========================================
# Topic : Type Conversion
# =========================================

# Integer to float
a = 10

b = float(a)

print(b)

print(type(b))

# Float to integer
x = 5.9

y = int(x)

print(y)

# Integer to string
num = 100

s = str(num)

print(s)

print(type(s))

# String to integer
age = "21"

real_age = int(age)

print(real_age + 5)

# Real life example
price = "500"

gst = 50

total = int(price) + gst

print("Total Price =", total)