"""KarpenkoNickA1Q2
COMP 1012 SECTION A01
INSTRUCTOR Saulo Santos
ASSIGNMENT: A1 Question 2
AUTHOR Nick Karpenko
VERSION 2026-Oct-8
PURPOSE: To find which day of the week a date is using Zellers algorithim
"""
#This boolean controls if the program would run again
tryAgain = True
#At the end, the user is prompted to enter another date, which changes tryAgain and dictates if the loop should continue
while tryAgain:
    #---------------------------------------------------------------------------------------------------------------
    #Declaring variables
    #---------------------------------------------------------------------------------------------------------------
    #MONTHS are the diffrent months starting from march because Zellers algorithim starts conuting from march
    MONTHS = ["march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "january", "february"]
    #The maximum dates each month holds, i.e march has 31, april 30, and February 29 (This is in case the user enters a leap year, if they don't they are reprompted to enter a date that is < 29)
    MONTH_BOUNDS = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 29]
    #Weekdays as dictated by Zellers algorithim, which starts from 0 = sunday, 1 = saturday,..., and 6 = friday 
    WEEKDAYS = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    
    #Booleans control wether to loop the user input for the different variables (Month, date, and year)
    enteringMonth = True
    enteringDate = True
    enteringYear = True
    
    #The different variables used in zellers algorithim
    #NumA starts at 3 because zellers algorithim starts counting months at march = 3
    numA = 3
    numB = 0
    numC = 0
    numD = 0
    
    #Set to true later on if the year is a leap year
    isLeapYear = False
    
    #Index of what month it is, 0 = march, 1 = april,..., 11 = february. This connects MONTHS and MONTH_BOUNDS
    monthIndex = 0
    
    #---------------------------------------------------------------------------------------------------------------
    #Getting the month
    #---------------------------------------------------------------------------------------------------------------
    
    #Because enteringMonth is set to true at the start of each "tryAgain" loop, this while loop will run until the user enters a recognised month
    while enteringMonth:
        
        #Makes numA = 3, if user didn't enter a valid month, then numA is reset to initial value
        numA = 3
        #Usermonth stores the month which the user inputs
        userMonth = input("Please enter the month: ")
        
        #checks if the userMonth is the same as any of the recognised months
        for item in MONTHS:
            
            if userMonth.lower() == item:
                #Because numA started counting at 3, the monthIndex has to correct for it and thats why there is the -3
                monthIndex = numA - 3
                #To exit the loop and not write the error message
                enteringMonth = False
            #so that numA doesn't increment once a month is recognised
            elif enteringMonth:
                #numA is incremented by 1 because each time this loops it moves on to the next month
                numA += 1
                
        if enteringMonth:
            #prints error message if no valid month was entered
            print("Please try again and enter a valid month")
            
    #---------------------------------------------------------------------------------------------------------------
    #Getting the date
    #--------------------------------------------------------------------------------------------------------------- 
    
    #Because enteringDate is set to true at teh start of every "tryAgain" loop, this while loop will always run       
    while enteringDate:
        
        #casts date input to int numB
        numB = int(input("Please enter the date: "))
        
        #as long as the date (numB) is greater than 0 and less than or equal to the maximum date of the month selected previously, this loop exits
        if numB > 0 and numB <= MONTH_BOUNDS[monthIndex]:
            enteringDate = False
            
        #Restarts loop if numB was out of bounds
        else:
            print("Please enter a valid date for the month you chose")
            
    #---------------------------------------------------------------------------------------------------------------
    #Getting the year
    #--------------------------------------------------------------------------------------------------------------- 
    
    while enteringYear:
        #yearToSlice is the year that will be spliced to find numC and numD
        yearToSlice = input("Please enter the year: ")
        #Year the user has entered but in int form
        userYear = int(yearToSlice)
        
        #If statement to make sure the user inputted a 4 digit year
        if userYear >= 1000 and userYear <= 9999:
            
            #Zellers algorithim calculates January and february as being in the previous year, and since monthIndex 
            #of january is 10 and of february it is 11, and numA = monthIndex +3, this if statement checks if numA
            #is greater than 13 and makes yearToSlice (which is where numC and numD are extracted from) the previous year
            if numA >= 13:
                yearToSlice = str(userYear - 1)
            #Checks if user year is leap year (divisible by 4 but not by 100 or divisble by 400)
            if (userYear % 4 == 0 and userYear % 100 != 0) or userYear % 400 == 0:
                isLeapYear = True
            
            #numC is the last 2 digits of the year, so it slices from the third digit to the end
            numC = int(yearToSlice[1:])
            #num D is the first two digits of the year so it slices up to (but not including) the third digit
            numD = int(yearToSlice[:2])
            enteringYear = False
            
        else:
            #prints error message 
            print("Please input a 4 digit year")
    
    #Pretty much an if stattment that loops. if it isn't a leap year (so february only has 28 days) and the month is
    #February and the date (numB) is greater than 28 (which means 29 or above and thus not in the month of february)
    #and is less than or equal to 0 (which cant be a date because there is no day 0 or -1 in february), this loops
    #and asks for a new date until conditions are satisfied
    while not isLeapYear and monthIndex == 11 and numB > 28 and numB <= 0:
        numB = int(input("Because this year is not a leap year the date previously entered is not possible, please enter a new date for this month: "))
    
    #---------------------------------------------------------------------------------------------------------------
    #Calulating the date and restarting program
    #--------------------------------------------------------------------------------------------------------------- 
    
    #Formula for Zeller's algorithim (whoose output is 0 = saturday, 1 = sunday, 2 = monday,..., 6 = friday 
    # which corresponds to the indeces of WEEKDAYS)
    numWeekday = int(((13 * (numA + 1) / 5) + (numC / 4) + (numD / 4) + numB + numC + (numD * 5))%7)
    
    #prints out the final output
    print("{} {}, {} is a {}".format(MONTHS[monthIndex], numB, userYear, WEEKDAYS[numWeekday]))
    
    #If the user inpus anything but "y", the main loop ends and program is terminated
    if input("Would you like to enter another date? (y/n): ") != "y":
        tryAgain = False
        
print("End of processing")