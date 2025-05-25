# Creating a set
marks = set()

marks.add(89)
marks.add(70)
marks.add(97)
marks.add(100)

print(marks)

# Set methods
print(len(marks)) # returns length of the set

marks.remove(70) # removes the element and updates the set
print(marks)

print(marks.pop()) # removes an element and returns the element released 
print(marks)

print(marks.union({89,79,100})) # performs union on the set

print(marks.intersection({89,100})) # performs intersection on the set

marks.clear() # Clears the set elements
print(marks)

# These functions do not update set but return a new set.