message = "Stuff and catanllamo"
wordToFind = "catan"
wordIndex = message.find(wordToFind)
extractedWord = message[wordIndex:wordIndex+len(wordToFind)]
print(extractedWord)
result = 5.12345
print("{:.4f}".format(result))