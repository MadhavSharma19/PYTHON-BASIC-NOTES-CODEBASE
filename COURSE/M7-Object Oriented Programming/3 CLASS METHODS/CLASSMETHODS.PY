class Employee:
    company = "TechCorp"      # Class variable
    employee_count = 0


    def __init__(self, name, salary):
        self.name = name       # Instance variable
        self.salary = salary
        Employee.employee_count += 1


    # Instance method - accesses instance data via self
    def get_info(self):
        return f"{self.name} earns {self.salary} at {self.company}"


    # Class method - accesses class data via cls
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name


    @classmethod
    def get_count(cls):
        return f"Total employees: {cls.employee_count}"


    # Static method - no access to instance or class data
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)


print(e1.get_info())            # Alice earns 50000 at TechCorp
Employee.change_company("NewCorp")
print(e1.get_info())            # Alice earns 50000 at NewCorp
print(Employee.get_count())     # Total employees: 2
print(Employee.is_valid_salary(50000))  # True
