markFile = open("marks.csv")
markFile.readline()
assignmentMarks = []
testMarks = []
for line in markFile:
    line = line.strip()
    assignmentMarks.append(int(line.split(",")[1]))
    testMarks.append(int(line.split(",")[2]))
maxAsignMark = assignmentMarks[0]
minAssignMark = assignmentMarks[0]
totalAssignMark = 0
for mark in assignmentMarks:
    if mark > maxAsignMark:
        maxAsignMark = mark
    elif mark < minAssignMark:
        minAssignMark = mark
    totalAssignMark += mark
avgAssignMark = totalAssignMark/len(assignmentMarks) 
print(f"Average mark: {avgAssignMark}, min mark: {minAssignMark}, max assign mark: {maxAsignMark}")
markFile.close()