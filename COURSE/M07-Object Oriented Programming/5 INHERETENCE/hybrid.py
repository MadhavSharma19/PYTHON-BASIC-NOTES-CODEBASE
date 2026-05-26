# ── Hybrid Inheritance Example ──
# Combines Hierarchical + Multiple Inheritance


# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")




# Hierarchical: Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


    def study(self):
        print(f"{self.name} is studying (ID: {self.student_id})")




# Hierarchical: Staff also inherits from Person
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


    def work(self):
        print(f"{self.name} works in {self.department}")




# Multiple: TeachingAssistant inherits from BOTH Student and Staff
class TeachingAssistant(Student, Staff):
    def __init__(self, name, age, student_id, department, subject):
        Student.__init__(self, name, age, student_id)
        Staff.__init__(self, name, age, department)
        self.subject = subject


    def assist(self):
        print(f"{self.name} is a TA for {self.subject}")




# Usage
ta = TeachingAssistant("Alice", 24, "S101", "Computer Science", "Python")


ta.display()    # Name: Alice, Age: 24         (from Person)
ta.study()      # Alice is studying (ID: S101) (from Student)
ta.work()       # Alice works in Computer Science (from Staff)
ta.assist()     # Alice is a TA for Python     (own method)


# View Method Resolution Order
print(TeachingAssistant.__mro__)
# (<class TeachingAssistant>, <class Student>, <class Staff>, <class Person>, <class object>)
