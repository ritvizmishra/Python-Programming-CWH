marksList = []

# Sorting the list from input
for i in range(1,7):
    studentMarks = input(f"Student #{i}, please enter your marks: ")
    marksList.append(int(studentMarks))

marksList.sort()
print(marksList)

# Summing up the marks
'''totalMarks = 0
for i in range(1,7):
    totalMarks += marksList[i-1]
    
print(totalMarks)'''

print(sum(marksList))
