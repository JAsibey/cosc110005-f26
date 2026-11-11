"""
Function Excercise: Decode a message.
Name: Assignment #2
Author: Jonathan Osei-Asibey
Date: 2026-11-10
Class Code: COSC-1100
"""

def Initialize():
    StringInput = str(input("Please enter a string: "))
    try:
        if not StringInput:
            raise ValueError("Input cannot be empty.")
        else:
            GetUserInput(StringInput)
            return StringInput
    except ValueError as e:
        print(f"Error: {e}")
        return None

def GetUserInput(StringInput):
    try:
        UserInput = int(input("1) Encode Text \n" + "2) Decode Text \n" + "3) Exit \n" + "Please select an option (1-3): "))

        if UserInput == 1:
         # Call the function to encode text
           EncodeText(StringInput)
        elif UserInput == 2:
         # Call the function to decode text
           DecodeText(StringInput)
        elif UserInput == 3:
        # Exit the program
            print("Exiting the program.")
        return UserInput
    
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return None


def EncodeText(StringInput):
    print("Encoding text... (functionality not implemented yet)")


def DecodeText(StringInput):
    print("Decoding text... (functionality not implemented yet)")

Initialize()