'''
You're building a system for a company.
Create two classes:
1. Employee
Attributes: name, salary
Method: display() → prints name and salary

2. Manager (inherits from Employee)
Additional Attribute: department
Override display() method to also print the department
Use super() to reuse the display() method from Employee
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"{self.name} earns {self.salary} ",end='')
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"being in {self.department} department.")
        
a = Manager('Ritviz', 100000, 'IT')
a.display()