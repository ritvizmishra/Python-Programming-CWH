class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"{self.i}x, {self.j}y")
        
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"{self.i}x, {self.j}y, {self.k}z")    
    
a = ThreeDVector(2,3,1)
a.show()
b = TwoDVector(4,6)
b.show()