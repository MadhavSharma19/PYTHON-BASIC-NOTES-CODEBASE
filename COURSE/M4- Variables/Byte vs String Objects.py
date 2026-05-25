# =========================================
# Topic : Byte vs String Objects
# =========================================

# String object
name = "Python"

print(name)

print(type(name))

# Byte object
data = b"Python"

print(data)

print(type(data))

# Accessing byte values
print(data[0])

print(data[1])

# Converting string into bytes
text = "Hello"

byte_text = text.encode()

print(byte_text)

# Converting bytes into string
original = byte_text.decode()

print(original)