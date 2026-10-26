dataSet = [99,15,26,15,8,10,27,8,96,69]
#[0,15,15,26,8]
for i in range(1,len(dataSet)):
    sortingNum = dataSet[i]
    j = i-1
    while j >= 0 and dataSet[j] < sortingNum:
        dataSet[j+1] = dataSet[j]
        j -= 1
    dataSet[j+1] = sortingNum
print(dataSet)


