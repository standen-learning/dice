#!/usr/bin/env python
#coding=utf-8

#This application simulates dice.  A user enters a number of dice
#they would like to roll and then generates a random number for 
#each die.  It then prints a virtual die for each number to the
#console.
#Note: This is from a tutorial.  I have followed these instructions
#   however, I have implemented my own logic.  Such as a constant
#   loop until the user quits the program.  I also used a main()
#   function for running the code.
#Link to tutorial: 
#   https://realpython.com/python-dice-roll/

#imports
import random
from turtle import width

#Global Constants
#DICE_ART stores all of the ASCII art for the dice.
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

#Function: main
#   Arguments: N/A
#   Variables: number_dice_prompt, dice_roll, dice_face_diagram
#   Return: N/A
#   Calls: prompt_user, roll_dice, generate_dice_faces
#   Called By: N/A
def main():
    #prompt user
    print("Welcome!!!")
    number_dice_prompt = prompt_user()

    #if user enters q, prompt_user returns 0, which will end the loop
    #and quit the program.
    while number_dice_prompt != 0:
        #if promp_user enters an invalid character, it will return -1
        #and run prompt_user again.
        if number_dice_prompt == -1:
            number_dice_prompt = prompt_user()
        else:
            dice_roll = roll_dice(number_dice_prompt)
            dice_face_diagram = generate_dice_faces(dice_roll)
            print(f"\n{dice_face_diagram}")
            number_dice_prompt = prompt_user()
    print("Thanks for playing.  See you next time!!!")
    exit()


#Function: prompt_user
#   Arguments: N/A
#   Variables: VALIDATION, QUIT_VALIDATION, num_dice_input, format_num_dice_input
#   Return: returns an integer value between 1 and 6
#   Calls: N/A
#   Called By: main
def prompt_user():
    VALIDATION = ["1", "2", "3", "4", "5", "6"] #for validating input
    QUIT_VALIDATION = ["q", "Q"]

    #prompt user
    num_dice_input = input("How many dice would you like to roll?\nPlease pick a number between 1 and 6 only.\nTo quit the program, press Q.\n")

    format_num_dice_input = num_dice_input.strip() #strip any space and \n characters.

    #validate input, if not valid, rerun function.
    if format_num_dice_input in VALIDATION:
        return int(format_num_dice_input)
    elif format_num_dice_input in QUIT_VALIDATION:
        return 0
    else:
        print("Your input is invalid.  Please try again.")
        return -1


#Function: roll_dice
#   Arguments: number_of_dice
#   Variables: roll_results, roll
#   Return: roll_results - A list of random integers each between 
#       1 and 6 for each dice.
#   Calls: N/A
#   Called By: main
def roll_dice(number_of_dice):
    roll_results = []
    i = 0
    while i < number_of_dice:
        roll = random.randint(1, 6)
        roll_results.append(roll)
        i = i + 1
     
    return roll_results

#Function: get_dice_faces
#   Arguments: dice_values
#   Variables: dice_faces
#   Return: dice_faces: a list that contains all of the 
#       art for each dice.
#   Calls: N/A
#   Called By: generate_dice_faces
def get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

#Function: get_dice_faces_rows
#   Arguments: dice_faces
#   Variables: dice_faces_rows, row_component, row_string
#   Return: dice_faces_rows - A list with each row formatted for dice face.
#   Calls: N/A
#   Called By: generate_dice_faces
def get_dice_faces_rows(dice_faces):
    dice_faces_rows = []

    for row_index in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_index])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    return dice_faces_rows

#Function: generate_dice_faces
#   Arguments: dice_values
#   Variables: dice_faces, dice_faces_rows, width, diagram_header dice_faces_diagram
#   Return: dice_faces_diagram - A string formatted for printing of each die's face.
#   Calls: get_dice_faces, get_dice_faces_rows
#   Called By: main
def generate_dice_faces(dice_values):
    dice_faces = get_dice_faces(dice_values)
    dice_faces_rows = get_dice_faces_rows(dice_faces)

    #Generate a header for Results
    width = len(dice_faces_rows[0])
    diagram_header = "RESULTS".center(width, "~")

    #Generate diagram
    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

#Run main
main()

#Function info template:

#Function: f_ name
#   Arguments: 
#   Variables: 
#   Return: 
#   Calls: 
#   Called By: