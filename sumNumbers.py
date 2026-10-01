totalSum = 0
wantsContinue = True
choice = input("Enter a number or q to quit: ")
if(choice == "q"):
    wantsContinue = False
elif(choice.isnumeric()):
    totalSum = totalSum + int(choice)
else:
    print("Thats not a number! Try again")
while wantsContinue:
    choice = input("Enter another number or q to quit: ")
    if(choice == "q"):
        wantsContinue = False
    elif(choice.isnumeric()):
        totalSum = totalSum + int(choice)
    else:
        print("Thats not a number! Try again")
print(f"Sum of all inputted numbers is: {totalSum}")