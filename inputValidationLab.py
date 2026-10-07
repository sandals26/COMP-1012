enteringNum = True
userNum = ""
numItems = 0
numCost = 0
while enteringNum:
    userNum = input("please enter the number of items: ")
    if userNum.isnumeric():
        numItems = int(userNum)
        enteringNum = False
    else:
        print("Please enter a valid number!!!")
enteringNum = True
while enteringNum:
    userNum = input("please enter the cost per item in cents: ")
    if userNum.isnumeric():
        numCost = int(userNum)
        enteringNum = False
    else:
        print("Please enter a valid number!!!")
askingMember = True
isMember = False
while askingMember:
    userInput = input("Are you a member? (yes/no): ")
    if userInput.lower() == "yes":
        isMember = True
        askingMember = False
    elif userInput.lower() == "no":
        isMember = False
        askingMember = False
    else:
        print("Please answer 'yes' or 'no' only")
costPerDollar = numCost/100
totalCost = 0
if numItems >= 20:
    totalCost = (costPerDollar * 0.8) * numItems
elif numItems > 20 and numItems >= 10:
    totalCost = (costPerDollar * 0.9) * numItems 
else:
    totalCost = costPerDollar * numItems
if isMember and numItems >= 10:
    totalCost = totalCost * 0.75
elif isMember:
    totalCost = totalCost * 0.85
print(f"The total cost is {totalCost}")