userInput = input("Enter 'q' to quit, 's' to square, and 'r' to square root: ")
if userInput == "s":
    numberToSquare = input("Input a positive integer: ")
    if userInput.isnumeric():
        print(f"The number squared is equal to {int(userInput)**2}")
    else:
        print("Please input a positive")
while userInput != "q":
    userInput = input("Enter 'q', 's', or 'r': ")