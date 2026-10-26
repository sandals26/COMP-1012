myFile = open("Week5Traffic.csv")
carList = dict()
passesPerHour = dict()
for line in myFile:
    currentCar = line.strip().split(",")
    timeTuple = currentCar[1].split(":")
    timeTuple[0] = int(timeTuple[0])
    timeTuple[1] = int(timeTuple[1])
    if currentCar[0] not in carList:
        carList[currentCar[0]] = []
        carList[currentCar[0]].append(timeTuple)
    else:
        carList[currentCar[0]].append(timeTuple)
    if timeTuple[0] not in passesPerHour:
        passesPerHour[timeTuple[0]] = 1
    else:
        passesPerHour[timeTuple[0]] += 1
mostSeen = ["", 0]
for item in carList:
    if len(carList[item]) > mostSeen[1]:
        mostSeen[0] = item
        mostSeen[1] = len(carList[item])
print(carList)
print(passesPerHour)
print(mostSeen)
print("Hours\tNum cars")
for hour in range(0,23):
    if hour not in passesPerHour:
        print("{}\t0".format(hour))
    else:
        print("{}\t{}".format(hour, passesPerHour[hour]))
print("Most seen car is {} with a total number of passes of {}".format(mostSeen[0], mostSeen[1]))