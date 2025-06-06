# Create a class employee and add salary and increment props to it
# Good for understanding.

class Employee:
    def __init__(self, salary):
        self.salary = salary
        self.newSalary = salary
    
    @property
    def increment(self):
       return f"Salary = {self.salary}\nNew salary = {self.newSalary}"
        
    @increment.setter
    def increment(self, inc):
        self.newSalary = self.salary * inc
        
emp = Employee(1000)
emp.increment = 1.2
print(emp.increment)