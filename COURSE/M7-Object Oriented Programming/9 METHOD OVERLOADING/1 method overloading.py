# =========================================
# Topic : Method Overloading
# =========================================

# Python does not support true
# method overloading directly

# We use default arguments or *args

class Sum:

    def add(self, *a):

        print(sum(a))

# Creating object
s1 = Sum()

# Different number of arguments
s1.add(10, 20)

s1.add(10, 20, 30)

s1.add(10, 20, 30, 40)