# import ramdom
# define a function to roll the  dice 
# create a dictionarythat will draw the dice
# create a while loop
# get user input 

import random

def rol_dice():
    
    roll = str(input('Roll dice? (Yes /No): '))
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print('Dice rolled: {} and {}'.format(dice1, dice2))
        
        roll =  input('Roll again? (Yes /No): ')
        
        
rol_dice()
    
