'''
## Think of `self` and `value` like Boxes

| Box Name | What's Inside?              | Used As                |
|----------|-----------------------------|------------------------|
| `self`   | First number (object `m`)   | You're inside this one |
| `value`  | Second number (object `n`)  | The one you're adding  |

Each box has a tag `real` and `imaginary` on it that holds the parts of the number.
'''

# Adding and multiplying complex numbers:
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def representComplex(self):
        print(f"The complex number is {self.real} + {self.imaginary}i.")
        
    def __add__(self, value):
        return f"\nThe sum of the two numbers is {self.real + value.real} + {self.imaginary + value.imaginary}i."
    
    def __mul__(self, value):
        real = self.real * value.real - self.imaginary * value.imaginary
        imag = self.real * value.imaginary + self.imaginary * value.real
        return f"The product of the two numbers is {real} + {imag}i."
    
m = Complex(int(input("Enter first num: ")), int(input("Enter second num: ")))
n = Complex(int(input("Enter first num: ")), int(input("Enter second num: ")))

m.representComplex()
n.representComplex()

print(m + n)
print(m * n)