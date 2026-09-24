lyrics = input("WabaLabaDooDad: ")
"""firstWord = lyrics[:lyrics.find(" ")]
print(firstWord)"""
lyricWords = []
startingIndex = 0
for i in range(len(lyrics)):
    if lyrics[i] == " " and len(lyrics) != i+1:
        lyricWords.append(lyrics[startingIndex:i])
        startingIndex = i+1
if lyrics[-1] != " ":
    lyricWords.append(lyrics[startingIndex:])
else:
    lyricWords.append(lyrics[startingIndex:-1])
print(lyricWords[0])
print(lyricWords[2])
print(lyricWords[len(lyricWords)-1])