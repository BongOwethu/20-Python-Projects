# import ramdom
# define a function to roll the  dice 
# create a dictionarythat will draw the dice
# create a while loop
# get user input 

import random

def rol_dice():
    
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }
    roll = str(input('Roll dice? (Yes /No): '))
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print('Dice rolled: {} and {}'.format(dice1, dice2))
        
        roll =  input('Roll again? (Yes /No): ')
        
        
rol_dice()
    
