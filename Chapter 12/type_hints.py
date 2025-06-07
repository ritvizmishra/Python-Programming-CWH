'''
1. Improves Code Readability
2. Helps Catch Bugs Early (via linters like MyPy)
3. IDE Auto-completion and Tooling
4. Great for Collaboration
'''

from typing import List, Tuple, Dict, Union

# type hint on variables
num : int = 5
print(num)

# type hint on functions
def sum(a : int, b : int) -> int:
    return a + b
print(sum(10,19))

# type hint on lists
numbers : List[int] = [1,2,4,5,3]
print(numbers)

# type hint on tuples
person : Tuple[str, int] = ("Ritviz", 24)
print(person)

# type hint on dictionary
scores : Dict[str, int] = {
    "A" : 9,
    "B" : 7,
    "C" : 3
}
print(scores)

# type hint on Union
identifiers : Union[str, int] = 'ID122'
print(identifiers)




