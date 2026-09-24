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
spaceAfterLetter = lyrics.find(" ",firstLetter) +1
secondLetter = lyrics.find(selectedLetter, spaceAfterLetter)
secondLetterStart = lyrics.rfind(" ",0,secondLetter) +1
secondLetterEnd = lyrics.find(" ", secondLetter)
secondLetterWord = lyrics[secondLetterStart:secondLetterEnd]
print(secondLetterWord)
secondLetterWord = lyrics[lyrics.rfind(" ", 0, secondLetter)+1:lyrics.find(" ", secondLetter)]
print(secondLetterWord)