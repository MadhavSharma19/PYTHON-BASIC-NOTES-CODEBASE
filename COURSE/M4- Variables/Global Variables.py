# =========================================
# Topic : Global Variables
# =========================================

# Global variable
school = "DAV School"

# Function
def student():

    # Accessing global variable
    print("School Name =", school)

# Calling function
student()

# Global variables can be used everywhere

def teacher():

    print("Teacher also works in", school)

teacher()

# Updating global variable

def update():

    global school

    school = "MITS"

update()

print("Updated School =", school)