# ask user if the want to generate a password or not
# if yes, we ask for password length
# generate password then print password
# if no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()') # these are the chracters we ant to generate from

def generate_password():
    password_length = int(input(' (0_0) Password length: '))
    
    random.shuffle(characters)   # shuffle list
    
    password =  [] # make password an empty list 
    
    for x in range(password_length):
        password.append(random.choice(characters))    
        
    random.shuffle(password) #shuffle it again
                   
    password = "".join(password) #join the letters
    
    print(password)
    
option = input('(0_0) Do you want to generate a password(y/n)? ')

if option == 'y' or option == 'yes':
    generate_password()
elif option == 'n' or option == 'no':
    print('Goodbye! :)')
    quit()
else:
    print('Invalid input, please type y for yes or n for no. ')
    quit()