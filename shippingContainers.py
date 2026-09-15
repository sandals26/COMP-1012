numWidgets = 73
hugeContainers = 0
largeContainers = 0
mediumContainers = 0
smallContainers = 0
while numWidgets > 0:
    if numWidgets >= 50:
        numWidgets -= 50
        hugeContainers += 1
    elif numWidgets >= 20:
        numWidgets -= 20 
        largeContainers += 1
    elif numWidgets >= 5:
        numWidgets -= 5
        mediumContainers += 1
    else:
        numWidgets -= 1
        smallContainers += 1
print("To ship {} widgets, use {} huge containers, {} large containers, {} medium containers, and {} small containers".format(numWidgets, hugeContainers, largeContainers, mediumContainers, smallContainers))