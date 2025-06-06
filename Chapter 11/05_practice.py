class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(box_1, box_2):
        new_i =  box_1.i + box_2.i
        new_j =  box_1.j + box_2.j
        new_k =  box_1.k + box_2.k
        
        return f"Sum of vectors: {new_i}i + {new_j}j + {new_k}k"
    
    def __mul__(box_1, box_2):
        new_i =  box_1.i * box_2.i
        new_j =  box_1.j * box_2.j
        new_k =  box_1.k * box_2.k
        
        return f"Dot product of vectors: {new_i + new_j + new_k}"
    
    def __len__(self):
        return 3
    
m = Vector(1,2,3)
n = Vector(4,5,6)

print(m+n)
print(m*n)

print(f"The dimension of vector m is {len(m)}.")