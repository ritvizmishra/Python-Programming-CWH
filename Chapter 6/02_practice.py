subjectOneMarks = int(input(f"Enter subject 1 marks: "))
subjectTwoMarks = int(input(f"Enter subject 2 marks: "))
subjectThreeMarks = int(input(f"Enter subject 3 marks: "))

aggregateMarks = subjectOneMarks + subjectTwoMarks + subjectTwoMarks
aggregatePercentage = (aggregateMarks/400)*100

if(aggregatePercentage >= 40 and subjectOneMarks >= 33 and subjectTwoMarks >= 33 and subjectThreeMarks >= 33):
    print("CONGRATULATIONS! YOU PASSED!")
else:
    print("Hard Luck!")

