studentGrades = {123: [99,99,98,96], 12:[93,94,95], 1234:[91,92,87,56,99,100]}
enteringNum1 = True
student1Key = 0
while enteringNum1:
    userNum = int(input("Student num: "))
    if userNum in studentGrades:
        student1Key = userNum
        enteringNum1 = False
student1Avg = sum(studentGrades[student1Key])/len(studentGrades[student1Key])