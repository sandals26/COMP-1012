myFile = open("file.txt")
words = []
line = 0
for aLine in myFile:
    numberOfVowels = 0
    splitLine = aLine.split()
    for word in splitLine:
        words.append(word)
    for letter in aLine:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            numberOfVowels += 1
    print(f"Line {line} has {len(splitLine)} words and {numberOfVowels} vowels")
    line += 1
print(words)
totalWordChar = 0
for item in words:
    totalWordChar += len(item)
averageCharCount = totalWordChar/len(words)
myFile = open("file.txt")
charachtercount = len(myFile.read())
myFile = open("file.txt")
wordcount = len(myFile.read().split())
print(f"The file has {line + 1} lines, {charachtercount} charachters, {wordcount} words")
myFile.close()
