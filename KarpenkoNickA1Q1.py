"""KarpenkoNickA1Q1
COMP 1012 SECTION A01
INSTRUCTOR Saulo Santos
ASSIGNMENT: A1 Question 1
AUTHOR Nick Karpenko
VERSION 2026-Oct-6
PURPOSE: Find the batting average, the number of singles, and the performance rating of a baseball player 
"""

#Declares the template that the final output will use, with the batting average and single count being rounded to 4 decimal places
FINAL_OUTPUT = "The player had a batting average of {:.4f}, his performance was: {}, and he got {:.4f} singles"

#Gathering and storing data from the user
numAtBats = int(input("Please enter the number of at-bats: "))
numHits = int(input("Please enter the number of hits: "))
numDoubles = int(input("Please enter the number of doubles: "))
numTriples = int(input("Please enter the number of triples: "))
numHomeRuns = int(input("Please enter the number of home runs: "))

#Calculating the batting average
battingAverage = numHits / numAtBats

#Calculating the number of singles hit by substracting the other number of hit types from the total hits
singles = numHits - numDoubles - numTriples - numHomeRuns

#Declaring a playerperformance variable
playerPerformance = ""

#Checks to see at what range does the batting average lie in and giving the corresponding grading 
if battingAverage >= 0.3:
    playerPerformance = "Excellent"
    
elif battingAverage < 0.3 and battingAverage >= 0.25:
    playerPerformance = "Good"
    
elif battingAverage < 0.25 and battingAverage >= 0.2:
    playerPerformance = "Average"
    
else:
    playerPerformance = "Needs improvement"

#prints the final output formatted with the apropriate variables
print(FINAL_OUTPUT.format(battingAverage, playerPerformance, singles))

print("End of processing")