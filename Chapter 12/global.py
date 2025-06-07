'''
- The global keyword is used to modify a variable that is defined outside a function (i.e., at the global scope) from inside a function.
- By default, variables inside a function are local — they can't change global variables unless you explicitly tell Python to do so using global.

- Without global (better practice)
'''
count = 0

def increment():
    global count 
    count += 1
    
increment()
print(count)