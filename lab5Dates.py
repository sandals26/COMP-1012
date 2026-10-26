months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednseday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
monthEnd ={"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,"September": 30, "October": 31, "November": 30, "December": 31}
date = 0
def getMonth():
    month = int(input("What is the month: "))
    if month > 0 and month <= 12:
        return month
    else:
        return getMonth()
def getDay(month:str):
    day = int(input("What is the day: "))
    if day > 0 and day <= monthEnd[month]:
        return day
    else:
        return getDay(month)
def getYear():
    userYear = int(input("What is the year: "))
    if userYear >= 1900 and userYear <= 2100:
        print(userYear)
        return userYear
    else:
        return getYear()
def getWeekDay():
    weekday = int(input("What is the Weekday: "))
    if weekday > 0 and weekday <= 7:
        return weekday
    else:
        return getWeekDay()
userMonth = getMonth()
date = getDay(months[userMonth])
userDays = getWeekDay()
year = getYear()
print("The date is {}, {} {}, {}".format(days[userDays], months[userMonth], date, year))
