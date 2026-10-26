firstWord = input("First word: ")
secondWord = input("Second word: ")
dictOne = dict()
dictTwo = dict()
    
for letter in firstWord:
    
    if letter.isalnum:
        
        if letter.lower() in dictOne:
            dictOne[letter.lower()] += 1
            
        else:
            dictOne[letter.lower()] = 1
            
            
for letter in secondWord:
    
    if letter.isalnum():
        
        if letter.lower() in dictTwo:            
            dictTwo[letter.lower()] += 1
            
        else:
            dictTwo[letter.lower()] = 1
        
        
if set(firstWord) == set(secondWord):
    print("They are anagrams (set versino)")
else:
    print("They aint no anagrams (set version)")


if dictOne == dictTwo:
    print("They are anagrams (dict versino)")
else:
    print("They aint no anagrams (dict version)")