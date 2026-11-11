"""
Functions excercise: Turning arrays into functions.
Author: Jonathan Osei-Asibey
Date: 2026-11-11
Class Code: COSC-1100
"""

#This line is for the final GPA output to get the sum of the grades
import math
#This is the array that will hold the grades of the user
grades = [0,0,0]

#This asks the user to input their pre class activities grade and will check if the input is valid or not.
def GetGrades():
    try:
        grades[0] = int(input("Enter your pre class activities grade: "))
        MidTermGrade()
    except ValueError:
        if grades[0] < 0 or grades[0] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")
    GetGrades()

#This asks the user to input their mid term grade and will check if the input is valid or not.
def MidTermGrade():
    try:
        grades[1] = int(input("Enter your mid term grade: "))
        ClassExerciseGrade()
    except ValueError:
        if grades[1] < 0 or grades[1] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")
    MidTermGrade()

#This asks the user to input their class exercise grade and will check if the input is valid or not.
def ClassExerciseGrade():
    try:
        grades[2] = int(input("Enter your class exercise grade: "))
        PrintGrades()
    except ValueError:
        if grades[2] < 0 or grades[2] > 100:
            print("Please type in an answer higher than 100 and lower than 0.")
    ClassExerciseGrade()

def PrintGrades():
    #This prints out the grades of the user to the console.
    print("Your pre class activities grade is: ", grades[0])
    print("Your mid term grade is: ", grades[1])
    print("Your class exercise grade is: ", grades[2])

    #This gets the sum of the grades and divides it by the length of the array to get the average of the grades and prints it out to the user to get their final GPA.
    grades_average = sum(grades) / len(grades)
    if grades_average > 100:
        grades_average = 100
    elif grades_average < 0:
        grades_average = 0
    
    print(f"Your GPA is: {grades_average:.2f}%")         

GetGrades()