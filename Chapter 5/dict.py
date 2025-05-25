# Syntax of dictionary
pr = {
    "bench" : 90,
    "squat" : 110,
    "deadlift" : 160,
    "shoulder press" : 60
}

print(pr["bench"])

# Methods in dictionary
print(pr.items()) # -- returns all the items in form of tuples

print(pr.keys()) # -- returns a list of all the keys

pr.update({"bench" : 95}) # -- updates a key : value pair
print(pr)

print(pr.get("squat")) # -- returns a value for key