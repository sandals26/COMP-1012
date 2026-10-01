userInput = input("Your 5 letter word: ")
while len(userInput) != 5 or not userInput.isalpha():
    userInput = input("Does not match requirements, try again: ")