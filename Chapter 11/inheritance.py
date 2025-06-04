class Employee:
    def show(self):
        print(f"Company name is {self.company}.")
        
class Coder:
    def getName(self):
        print(f"Name of the programmer is {self.name}.") 
    
class Programmer(Employee, Coder):
    company = 'EY'
    name = "Anonymous"
    def showLang(self):
        print(f"{self.company} uses Python. The employee name is {self.name}.")
        
a = Programmer()
a.show()
a.getName()
a.showLang()
        
