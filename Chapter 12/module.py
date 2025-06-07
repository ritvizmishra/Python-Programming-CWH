'''
If code is run in this file, __name__ would be set to __main__. Otherwise, in other files it will show file_name.
'''

def helloWorld():
    print("hello world!")
    
helloWorld()

if __name__ == "__main__":
    print("Inside the module directory.")

print(__name__)
