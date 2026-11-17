"""
Function Excercise: Decode a message.
Name: Assignment #2
Author: Jonathan Osei-Asibey
Date: 2026-11-10
Class Code: COSC-1100
"""
#STEP 1: Get the string input from the user. Make sure to check if its valid or not.
#STEP 2: Get the user to input their option to either decode or encode the message. Make sure to check if its valid or not.
#STEP 3: If the user selects whatever they want, make sure the selection is valid.

#These are the Arrays for the alphabet and the AL Bhed language that will be used to decode or encode the message.
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Al_Bhed = ['Y', 'P', 'L', 'T', 'A', 'V', 'K', 'R', 'E', 'Z', 'G', 'M', 'S', 'H', 'N', 'C', 'D', 'X', 'B', 'U', 'F', 'J', 'W', 'Q', 'O', 'y', 'p', 'l', 't', 'a', 'v', 'k', 'r', 'e', 'z', 'g', 'm', 's', 'h', 'n', 'c', 'd', 'x', 'b', 'u', 'f', 'j', 'w', 'q', 'o']

#The main function that will prompt the user to input a valid string.
def Initialize():
    StringInput = str(input("Please enter a string: "))
    try:
        if not StringInput:
            raise ValueError("Input cannot be empty.")
        else:
            GetUserInput(StringInput)
            return StringInput
    except ValueError:
        return None

#The 2nd most important function will prompt the user to select an option to decode or encode their message, or leave the program.
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
        GetUserInput(StringInput)
        return None

#The function that will loop through the string and encode it to the AL Bhed language.
def EncodeText(StringInput):
    encoded_text = ""
    for char in StringInput:
        if char in Alphabet:
            index = Alphabet.index(char)
            encoded_text += Al_Bhed[index]
        else:
            encoded_text += char
    print(f"Encoded text: {encoded_text}")
    GetUserInput(StringInput)

#The function that will loop through the string and decode it to the alphabet language.
def DecodeText(StringInput):
    decoded_text = ""
    for char in StringInput:
        if char in Al_Bhed:
            index = Al_Bhed.index(char)
            decoded_text += Alphabet[index]
        else:
            decoded_text += char
    print(f"Decoded text: {decoded_text}")
    GetUserInput(StringInput)

#This is to actually start the program.
Initialize()