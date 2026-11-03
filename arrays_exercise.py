"""
Arrays excercise: Finding the GPA of a student.
Name: Finding the GPA of a student
Author: Jonathan Osei-Asibey
Date: 2026-11-03
Class Code: COSC-1100
"""

#This line is for the final GPA output to get the sum of the grades
import math
#This is the array that will hold the grades of the user
grades = [0,0,0]

#This asks the user to input their pre class activities grade and will check if the input is valid or not.
while True:
    try:
        grades[0] = int(input("Enter your pre class activities grade: "))
        break
    except ValueError:
        if grades[0] < 0 or grades[0] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")

#This asks the user to input their mid term grade and will check if the input is valid or not.
while True:
    try:
        grades[1] = int(input("Enter your mid term grade: "))
        break
    except ValueError:
        if grades[1] < 0 or grades[1] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")

#This asks the user to input their class exercise grade and will check if the input is valid or not.
while True:
    try:
        grades[2] = int(input("Enter your class exercise grade: "))
        break
    except ValueError:
        if grades[2] < 0 or grades[2] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")  

#This gets the sum of the grades and divides it by the length of the array to get the average of the grades and prints it out to the user to get their final GPA.
grades_average = sum(grades) / len(grades)
print(f"Your GPA is: {grades_average:.2f}%")         


    



            

