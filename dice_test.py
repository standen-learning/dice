#Unit testing for Dice class in the 
#dice_class.py file.
from dice_class import Dice

#function for running all test suites in this
#file.
def class_test():
    dice_roll_1()
    dice_roll_2()
    dice_roll_3()
    dice_roll_4()
    dice_roll_5()
    dice_roll_6()
    dice_roll_G()
    exit()

#Should return 1 dice face.
def dice_roll_1():
    roll_1 = Dice(1)
    print("Should generate 1 die.")
    print(roll_1.generate_dice_faces())

#Should return 2 dice faces.
def dice_roll_2():
    roll_2 = Dice(2)
    print("Should generate 2 dice.")
    print(roll_2.generate_dice_faces())

#Should return 3 dice faces.
def dice_roll_3():
    roll_3 = Dice(3)
    print("Should generate 3 dice.")
    print(roll_3.generate_dice_faces())

#Should return 4 dice faces.
def dice_roll_4():
    roll_4 = Dice(4)
    print("Should generate 4 dice.")
    print(roll_4.generate_dice_faces())

#Should return 5 dice faces.
def dice_roll_5():
    roll_5 = Dice(5)
    print("Should generate 5 dice.")
    print(roll_5.generate_dice_faces())

#Should return 6 dice faces.
def dice_roll_6():
    roll_6 = Dice(6)
    print("Should generate 6 dice.")
    print(roll_6.generate_dice_faces())

#Should raise an exception
def dice_roll_G():
    print("Should raise an exception.")
    try:
        roll_G = Dice(G)
        print(roll_G.generate_dice_faces())
    except:
        print("Value passed to constructor not an integer.")

class_test()