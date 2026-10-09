"""KarpenkoNickA1Q3
COMP 1012 SECTION A01
INSTRUCTOR Saulo Santos
ASSIGNMENT: A1 Question 3
AUTHOR Nick Karpenko
VERSION 2026-Oct-9
PURPOSE: To find the number of occurences of a word in a file
"""

#---------------------------------------------------------------------------------------------------------------
#Declaring variables
#---------------------------------------------------------------------------------------------------------------

#The two names of the files being used, wordFileName is the file which contains teh words and storyFileName is the file with the story
wordFileName = input("Enter the name of the file which contains the words to count: ")
storyFileName = input("Enter the name of the file containing the story: ")

#Opens the two different files, also there is a version where the encoding isn't utf-8 i dont know which one you'd 
#want us to use so I used utf-8 and put the regular one in a comment
wordFile = open(wordFileName)
#storyFile = open(storyFileName)
storyFile = open(storyFileName, encoding="utf-8")

#Two lists, wordsToLookFor is the file which contains the list of words that are going to be conuted while wordsCount
# is the list of the amount of words counted in the story and where wordsCount[n] = the number of times wordsToLookFor[n]
# apears in the story file
wordsToLookFor = []
wordsCount = []

#---------------------------------------------------------------------------------------------------------------
#Counting words
#---------------------------------------------------------------------------------------------------------------

#Looks through the wordFile and creates 2 lists based on it
for line in wordFile:
    
    #Looks through the list that is created after removing the whitespace on the ends of the line and splitting the line
    for word in line.strip().split():
        #adds every word in the line to a list and makes a corresponding index in wordsCount
        wordsToLookFor.append(word)
        wordsCount.append(0)

#Goes line by line through the story file
for line in storyFile:
    
    #goes through every word on the line without the whitespace on the end
    for word in line.strip().split():
        
        #checks if the list wordsToLookFor contains the word and then increments the corresponding index of wordsCount
        if word in wordsToLookFor:           
            wordsCount[wordsToLookFor.index(word)] += 1

#Loops through every word that was looked for and prints the corresponding message for the word
for word in wordsToLookFor:
    
    #The wordsCount index is sinced to the index of wordsToLookFor so, taking the inex of where the word is in wordsToLookFor
    # and pluging in that into wordsCount to get the count of how much that word showed up
    print("The word \"{}\" occurs {} times".format(word, wordsCount[wordsToLookFor.index(word)]))
    
print("End of processing")