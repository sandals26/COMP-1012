def loadData(fileName:str):
    myFile = open(fileName)
    myFile.readline()
    tuplList = []
    for line in myFile:
        ttlLine = line.split(",")
        tuplList.append(tuple([float(ttlLine[8]), float(ttlLine[9]), float(ttlLine[10])]))
    return tuplList
def getAverages(list):
    sumMax = 0
    for i in list:
        sumMax += i[0]
    sumMax = sumMax/len(list)
    sumMin = 0
    for i in list:
        sumMin += i[1]
    sumMin = sumMin/len(list)
    sumMed = 0
    for i in list:
        sumMed += i[1]
    sumMed = sumMed/len(list)
    return tuple([sumMax, sumMin, sumMed])
def getExtremes(list):
    maxTemp = list[0][0]
    minTemp = list[0][1]
    for i in list:
        if i[0] > maxTemp:
            maxTemp = i[0]
        if i[1] < minTemp:
            minTemp = i[1]
    return tuple([maxTemp,minTemp])
listTemp = loadData("Week6WinnipegWeatherData.csv")
print(getAverages(listTemp))
print(getExtremes(listTemp))