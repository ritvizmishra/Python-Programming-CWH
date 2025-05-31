# Finding location of mined word:

with open("Log/logs.txt") as file:
    content = file.readlines()

lineNum = 1
for word in content:
    if "python" in word:
        print("true, in line: ", lineNum)
        break
    lineNum += 1
else:
    print("false")