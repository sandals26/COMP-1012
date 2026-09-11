"""DogoodRodneyA1Q1
COMP 1012 SECTION A01
INSTRUCTOR [Name of your instructor]
ASSIGNMENT: A1 Question 1
AUTHOR Nick Karpenko
VERSION 2026-Sep-11
PURPOSE: find the area and circumference of a circle given the radius
"""
PI = 3.14
radius= int(input("what is the radius of the circle?\n"))
area = PI * radius ** 2
circumference = 2 * PI * radius
print(f"The area of the circle is {area}, and the circumference is {circumference}")