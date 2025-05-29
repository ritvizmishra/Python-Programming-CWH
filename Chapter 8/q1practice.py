def greatestNum (a,b,c):
    max = None
    if max is None or max < a:
        max = a
        if max < b:
            max = b
            if max < c:
                max = c
    maxNum = print(f"The greatest of the three is {max}.")
    return maxNum

greatestNum(347,45,128)
