# _ is the default case (like else or default)

# Example 1
def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500: 
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(https_status(200))
print(https_status(404))
print(https_status(500))
print(https_status(403))

# Example 2
def coordinates(point):
    match point:
        case (0,0):
            return "Origin"
        case (0,y):
            return f"Lies on y-axis at a distance of {y} units."
        case (x,0):
            return f"Lies on x-axis at a distance of {x} units."
        case (x,y):
            if x > 0 and y > 0:
                return f"({x},{y}) lies in first coordinate."
            elif x < 0 and y > 0:
                return f"({x},{y}) lies in second coordinate."
            elif x < 0 and y < 0:
                return f"({x},{y}) lies in third coordinate."
            else:
                return f"({x},{y}) lies in fourth coordinate."
    
print(coordinates(point:=(0,0)))
print(coordinates(point:=(0,4)))
print(coordinates(point:=(4,0)))
print(coordinates(point:=(3,-9)))
print(coordinates(point:=(-2,1)))
print(coordinates(point:=(-4,-8)))