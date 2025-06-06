class MathOp:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, value):
        return self.num + value.num
        
n = MathOp(2)
m = MathOp(3)
print(n + m)