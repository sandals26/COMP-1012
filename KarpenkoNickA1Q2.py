tryAgain = True
while tryAgain:
    MONTHS = ["march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "january", "february"]
    MONTH_BOUNDS = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 29]
    WEEKDAYS = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    enteringMonth = True
    enteringYear = True
    enteringDate = True
    numA = 0
    numB = 0
    numC = 0
    numD = 0
    isLeapYear = False
    monthIndex = 0
    while enteringMonth:
        userMonth = input("Please enter the month: ")
        tempNumA = 3
        for item in MONTHS:
            if userMonth.lower() == item:
                numA = tempNumA
                monthIndex = numA - 3
                enteringMonth = False
            else:
                tempNumA += 1
        if enteringMonth:
            print("Please try again and enter a valid month")
    print(f"Month: {userMonth}, corresponding month: {MONTHS[monthIndex]}, numA = {numA}")
    while enteringDate:
        numB = int(input("Please enter the date: "))
        if numB > 0 and numB <= MONTH_BOUNDS[monthIndex]:
            enteringDate = False
        else:
            print("Please enter a valid date for the month you chose")
    while enteringYear:
        yearToSlice = input("Please enter the year: ")
        userYear = int(yearToSlice)
        if userYear >= 1000 and userYear <= 9999:
            if numA >= 13:
                userYear = userYear - 1
                yearToSlice = str(userYear)
            if (userYear % 4 == 0 and userYear % 100 != 0) or userYear % 400 == 0:
                isLeapYear = True
            numC = int(yearToSlice[1:])
            numD = int(yearToSlice[:2])
            enteringYear = False
    while not isLeapYear and monthIndex == 11 and numB > 28:
        numB = int(input("Because this year is not a leap year the date previously entered is not possible, please enter a new date for this month: "))
    print(f"numA {numA}, numB {numB}, numC {numC}, numD {numD}, and is leapyear = {isLeapYear}")
    numWeekday = int(((13 * (numA + 1) / 5) + (numC / 4) + (numD / 4) + numB + numC + (numD * 5))%7)
    print(numWeekday)
    print(f"Month is {MONTHS[monthIndex]}, month end is {MONTH_BOUNDS[monthIndex]}, and chosen date is {numB}, year is {userYear}, and the weekday is {WEEKDAYS[numWeekday]}")
    if input("Would you like to enter another date? (yes/no): ") != "yes":
        tryAgain = False