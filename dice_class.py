#Class: Dice
#Arguments: number_of_dice - integer
#Methods: 
#   generate_dice_faces - returns the final variable used to
#               print the dice faces to the terminal.
#   roll_dice - takes in number_of_dice variable and 
#               generates a random int value between
#               1 and 6 until number_of_dice is reached.
#   get_dice_faces - takes in the _roll variable and returns
#               a list of strings that represent a visual
#               die face.
#   get_dice_faces_rows - returns a formatted version of
#               the variable returned from get_dice_faces
#               that is usable for printing to the terminal.



#imports
import random

class Dice:
    #Constants
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

    #Constructor
    def __init__(self, number_of_dice):
        if isinstance(number_of_dice, int):
            self._num_dice = number_of_dice
            self._roll = self._roll_dice()
        else:
            raise TypeError('Value given to Dice constructor not an integer.')

    ######PRIVATE METHODS######

    #Function: _roll_dice
    #   Arguments: self
    #   Variables: roll_results, roll
    #   Return: roll_results - A list of random integers each between 
    #       1 and 6 for each dice.
    #   Calls: N/A
    #   Called By: constructor
    def _roll_dice(self):
        roll_results = []
        i = 0
        while i < self._num_dice:
            roll = random.randint(1, 6)
            roll_results.append(roll)
            i = i + 1
        
        return roll_results

    #Function: _get_dice_faces
    #   Arguments: self
    #   Variables: dice_faces
    #   Return: dice_faces: a list that contains all of the 
    #       art for each dice.
    #   Calls: N/A
    #   Called By: generate_dice_faces
    def _get_dice_faces(self, values):
        dice_faces = []
        for value in values:
            dice_faces.append(self.DICE_ART[value])
        return dice_faces

        #Function: _get_dice_faces_rows
    #   Arguments: self
    #   Variables: dice_faces_rows, row_component, row_string
    #   Return: dice_faces_rows - A list with each row formatted for dice face.
    #   Calls: N/A
    #   Called By: generate_dice_faces
    def _get_dice_faces_rows(self, dice_faces):
        dice_faces_rows = []

        for row_index in range(self.DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_index])
            row_string = self.DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)

        return dice_faces_rows
        

    ######PUBLIC METHODS######

    #Function: generate_dice_faces
    #   Arguments: dice_values
    #   Variables: dice_faces, dice_faces_rows, width, diagram_header dice_faces_diagram
    #   Return: dice_faces_diagram - A string formatted for printing of each die's face.
    #   Calls: get_dice_faces, get_dice_faces_rows
    #   Called By: main
    def generate_dice_faces(self):
        dice_faces = self._get_dice_faces(self._roll)
        dice_faces_rows = self._get_dice_faces_rows(dice_faces)

        #Generate a header for Results
        width = len(dice_faces_rows[0])
        diagram_header = "RESULTS".center(width, "~")

        #Generate diagram
        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        return dice_faces_diagram