# Mining a log and returning true/false

with open("Log/logs.txt") as file:
    content = file.read().lower()
if "python" in content:
    print("true")
else:
    print("false")