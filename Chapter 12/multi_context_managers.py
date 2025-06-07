'''
Basic Syntax (Python 3.x)
with open("file1.txt") as f1, open("file2.txt") as f2:
    data1 = f1.read()
    data2 = f2.read()
You can use commas to chain multiple context managers. All will be properly opened and closed (even if an error occurs in between).
'''

with (
    open('Chapter 9\\Files\\this.txt', "a") as file_1,
    open('Chapter 9\\Files\\this_02.txt', "a+") as file_2
):
    file_1.write('''
                 This is updated using multiple context manager in Ch 12.
                 ''')