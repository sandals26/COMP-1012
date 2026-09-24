lyrics = input("Song lyrics: ")
fristWord = lyrics[:lyrics.find(" ")]
lastWord = lyrics[lyrics.rfind(" ")+1:]
secondIndex = lyrics.find(" ") + 1
thirdIndex = lyrics.find(" ", secondIndex) + 1
thirdEnd = lyrics.find(" ", thirdIndex)
thirdWord = lyrics[thirdIndex:thirdEnd]
print(fristWord+" "+lastWord)
print(thirdWord)
selectedLetter = input("Selected letter: ")
firstLetter = lyrics.find(selectedLetter) + 1
secondLetter = lyrics.find(selectedLetter, firstLetter)
secondLetterStart = lyrics.rfind(" ",secondLetter) +1
secondLetterEnd = lyrics.find(" ", secondLetter)
secondLetterWord = lyrics[secondLetterStart:secondLetterEnd]
print(secondLetterWord)