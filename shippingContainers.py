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
print("To ship {} widgets, use {} huge containers, {} large containers, {} medium containers, and {} small containers".format(totalNumWidgets, hugeContainers, largeContainers, mediumContainers, smallContainers))