list1 = [3, 12, 18, 23, 26, 31, 34, 40]
list2 = [5, 8, 10, 11, 18, 23, 29]
index1 = 0
index2 = 0
lastIndex1 = -1
lastIndex2 = -1
commonElements = []
combinedList = []
while index1 < len(list1) and index2 < len(list2):
    if (list1[index1]) == (list2[index2]):
        commonElements.append(list1[index1])
        combinedList.append(list1[index1])
        print(f"Apending {list1[index1]} to combined list")
        index1 += 1
        index2 += 1
    elif (list1[index1]) < (list2[index2]):
        combinedList.append(list1[index1])
        print(f"Apending {list1[index1]} to combined list")
        index1 += 1
    elif (list1[index1]) > (list2[index2]):
        combinedList.append(list2[index2])
        print(f"Apending {list2[index2]} to combined list")
        index2 += 1
while index1 < len(list1):
    combinedList.append(list1[index1])
    index1 += 1
while index2 < len(list2):
    combinedList.append(list2[index1])
    index2 += 1
print(combinedList)
listInOne = combinedList
for item in commonElements:
    listInOne.pop(listInOne.index(item))
print(listInOne)