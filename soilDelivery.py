TRUCK_CAPACITY = 8
exitLoop = True
soilToBuy = 0
while exitLoop:
    userInput = input("How much soil in m^3 are you buying: ")
    if userInput.isnumeric():
        if int(userInput) >= 0:
            soilToBuy = int(userInput)
            exitLoop = False
soilcost = 0
if soilToBuy >= 50:
    soilcost = 10
elif soilToBuy >= 20:
    soilcost = 20
else:
    soilcost = 30
totalTrips = soilToBuy//TRUCK_CAPACITY
if soilToBuy % TRUCK_CAPACITY >= TRUCK_CAPACITY/2:
    totalTrips = soilToBuy//TRUCK_CAPACITY + 1
else:
    soilToBuy = soilToBuy - soilToBuy % TRUCK_CAPACITY
deliveryCost = 0
if totalTrips >= 10:
    deliveryCost = 80
else:
    deliveryCost = 100
totalSoil = 0
print(f"Final cost: {soilToBuy*soilcost + totalTrips*deliveryCost}")