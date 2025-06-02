# Class name is written in Pascal case:
    
class Employee:
    lang = "Java" # lang is a class attribute
    salary = 1020200 # salary is a class attribute
    
ritviz = Employee()
ritviz.name = "Ritviz Mishra" # name is an instance attribute
print(ritviz.name, ritviz.lang, ritviz.salary)

aditi = Employee()
aditi.name = "Aditi Singh" # name is an instance attribute
aditi.lang = 'Python' # takes preference over class attribute
print(aditi.name, aditi.lang, aditi.salary)

##################################################################
##################################################################

class CatPreparation:
    varc = 27
    lrdi = 39
    qa = 21
    def getMockScores(self):
        print(f'''\nGiven student has scored {self.varc} in VARC, {self.lrdi} in LRDI, and {self.qa} in QA.
              \nThe overall score is {self.varc + self.lrdi + self.qa}.''')
    
    # static method, doesn't need an object.
    @staticmethod 
    def greetStudent(): 
        print("Well Done!")

ritviz = CatPreparation()
ritviz.getMockScores()
ritviz.greetStudent()    
        
##################################################################
##################################################################

class SalesPersonInfo:
    def __init__(self, name, area, age):
        self.name = name
        self.area = area
        self.age = age
        print(f"\n{name} is active in {area} and is {age} years old.")
        
ritviz = SalesPersonInfo("Ritviz Mishra", "suburb", 24)