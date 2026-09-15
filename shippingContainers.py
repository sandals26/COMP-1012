"""NickKarpenkoA1Q1
COMP 1012 SECTION A01
INSTRUCTOR Saulo Q. Dos Santos
ASSIGNMENT: A01 Week 01 Activity 2
AUTHOR Nick Karpenko
VERSION 2026-Sep-15
PURPOSE: find the optimal numbers of huge, large, medium, and small containers to "ship" a number of widgets
"""
numWidgets = int(input("Number of widgets:"))
totalNumWidgets = numWidgets #total number of widgets, used for print statement
hugeContainers = 0
largeContainers = 0
mediumContainers = 0
smallContainers = 0
"""while numWidgets > 0:
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
        smallContainers += 1"""
hugeContainers = numWidgets//50 #50 is the amount of widgets a "huge container" could hold
numWidgets -= numWidgets//50 * 50
largeContainers = numWidgets//20 #20 is the amount of widgets a "large container" could hold
numWidgets -= numWidgets//20 * 20
mediumContainers = numWidgets//5#5 is the amount of widgets a "medium container" could hold
numWidgets -= numWidgets//5 * 5
smallContainers = numWidgets//1#1 is the amount of widgets a "small container" could hold
numWidgets -= numWidgets//1 
print("To ship {} widgets, use {} huge containers, {} large containers, {} medium containers, and {} small containers".format(totalNumWidgets, hugeContainers, largeContainers, mediumContainers, smallContainers))