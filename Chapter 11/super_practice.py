'''
Create two classes:
1. Shape
Method: area() → prints "Area not defined"
Method: display() → prints "This is a shape."

2. Circle (inherits from Shape)
Attribute: radius
Override:
area() → calculates and prints area of the circle (π * r^2)
display() → uses super().display() first, then prints "This is a circle."
'''

class Shape:
    def area(self):
        print("Area not defined.")
    
    def display(self):
        print("This is a shape.")
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area circle: {round((22/7) * (self.radius ** 2), 2)}")
        
    def display(self):
        super().display()
        print("This is a circle.")
        
s = Circle(5)
s.display()
s.area()