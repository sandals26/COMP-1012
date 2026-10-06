myFile = open("apple.txt", "rt")
lineList = myFile.readlines()
print(lineList[2])
myFile.close()