class Calculator:
    def __init__(self,name):
        print(f"Hello, {name}!")
    
    @staticmethod
    def getCube(num):
        return (num**3)
    
    @staticmethod
    def getSquare(num):
        return (num**2)
    
    @staticmethod
    def getSquareRoot(num):
        return (num**0.5)
    

# Need to create Calculator() objects for calling non-static methods.
ritviz = Calculator(input("Enter your name: "))

# No need to create Calculator() objects for calling static methods. 
print(Calculator.getCube(11))
print(Calculator.getSquare(14))
print(Calculator.getSquareRoot(9409))