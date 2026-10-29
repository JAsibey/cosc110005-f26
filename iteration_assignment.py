"""Assignment 1: Iteration: Finds the square roots of numbers in a given range."""
"""
Name: Finding the square roots of numbers
Author: Jonathan Osei-Asibey
Date: 2026-10-29
Class Code: COSC-1100
"""
#STEP 1: Make the header / title of the program
#STEP 2: Get the lower bound number from the user and check if it's valid as well
#STEP 3: Get the upper bound number from the user and check if it's valid as well
#STEP 4: Find the square root of the numbers in the given range and print them in a loop

#This is is for the output to detect for the square root of the numbers
import math

#This is for the header of the program
for i in range(1,30):
    print("*", end='')

print("\nSQUARE NUMBER FINDER")

for i in range(1,30):
    print("*", end='')

#Checks for the users input and later it checks if the input is valid or not, if not it specifies on what the user entered in wrong
while True:
    try:
        lowerbound = int(input("\nEnter the lower bound number: "))
        lresult = math.sqrt(lowerbound)
        break
    except ValueError:
        if lowerbound < 1 or lowerbound > 10000:
            print("Invalid input. Please enter a whole number between 1 and 10000.")

        if lowerbound.is_float():
            print("Invalid input. Please enter a valid whole number.")

        if lowerbound.is_string():
            print("Invalid input. Please enter a valid whole number.")

#Checks for the users input and later it checks if the input is valid or not, if not it specifies on what the user entered in wrong
while True:
    try:
        upperbound = int(input("Enter the upper bound number: "))
        uresult = math.sqrt(upperbound)
        break
    except ValueError:
        if upperbound < lowerbound or upperbound > 10000:
            print("Invalid input. Please enter a whole number between 1 and 10000.")

        if upperbound.is_float():
            print("Invalid input. Please enter a valid whole number.")

        if upperbound < 1 or upperbound > 10000:
            print("Invalid input. Please enter a whole number between 1 and 10000.")

        if upperbound.is_string():
            print("Invalid input. Please enter a valid whole number.")

#This is a loop that will find the square root of the numbers in the given range
for i in range(int(lowerbound), int(upperbound) + 1):
    print(math.sqrt(i), "()" + str(lowerbound), "squared)")