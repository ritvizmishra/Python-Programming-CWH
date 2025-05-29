'''
* * * * *
* * * *
* * *
* *
*
'''

def printPattern(num):
    if num == 0:
        return
    print("* " * num)
    printPattern(num-1)
    
printPattern(10)