import os

directory_path = "/" 
# '/' gives content of C drive; '.' gives current modules content.

try:
    contents = os.listdir(directory_path)

    # f stands for formatted string literal
    print(f"Contents of '{directory_path}' are: ")
    for items in contents:
        print(items)

except FileNotFoundError:
    print(f"The {directory_path} does not exist.")
    
except PermissionError:
    print(f"Access to {directory_path} denied.")
    
