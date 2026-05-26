# =========================================
# Topic: Default Constructor
# Real Life Scenario: Student Profile
# =========================================

class Student:

    # Default Constructor
    def __init__(self):

        

        self.name = "Aman"
        self.age = 20
        self.course = "Python"
    

    # Method to display details
    def show_details(self):

        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)


# Creating Object
s1 = Student()

# Calling Method
s1.self.name()