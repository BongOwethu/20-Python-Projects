import random

exit = False
user_points = 0
computer_points = 0

while exit == False:  
    options = ['rock','paper', 'scissors']
    user_input = input('Choose rock, paper, scissors or exit (9_9): ')  
    computer_input= random.choice(options)
    
    if user_input == 'exit':
        print('Goodbye!! (*_*)')
        print('Player Total score: '+ str((user_points)))
        print('Computer Total score: '+ str((computer_points)))
        exit = True
        
    if user_input == 'rock':
        if computer_input == 'rock':
            print('Your input is rock')
            print('Computer input is rock')
            print('Its a tie. (6_^)')
        elif computer_input == 'paper':
            print('Your input is rock')
            print('Computer input is paper')
            print('Computer wins! (0_0)')
            computer_points +=1
        elif computer_input == 'scissors':
            print('Your input is rock')
            print('Computer input is scissors')
            print('You wins! (^_^)')
            user_points +=1
        
    elif user_input == 'paper':
        if computer_input == 'rock':
            print('Your input is paper')
            print('Computer input is rock')
            print('You win! (^_^)')
            user_points +=1        
        elif computer_input == 'paper':
            print('Your input is paper')
            print('Computer input is paper')
            print('Its a tie. (6_^)')  
        elif computer_input == 'scissors':
            print('Your input is paper')
            print('Computer input is scissors')
            print('Computer win! (0_0)')
            computer_points +=1
            
    elif user_input == 'scissors':
        if computer_input == 'rock':
            print('Your input is scissors')
            print('Computer input is rock')
            print('Computer wins! (0_0)')
            computer_points +=1
                   
        elif computer_input == 'paper':
            print('Your input is scissors')
            print('Computer input is paper')
            print('You win! (^_^)')
            user_points +=1 
        elif computer_input == 'scissors':
            print('Your input is scissors')
            print('Computer input is scissors')
            print('Its a tie. (6_^)') 
            
    elif user_input != 'rock' or user_input !='paper' or user_input != 'scissors':
        print('Invalid input (*_*)')
              


