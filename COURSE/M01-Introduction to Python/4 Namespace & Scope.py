# =========================================
# Namespace & Scope
# =========================================

x = 100

def demo():

    x = 50

    print("\nLocal Scope =", x)

demo()

print("Global Scope =", x)