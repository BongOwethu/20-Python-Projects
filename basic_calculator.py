# define the functions:add,sub,mul,div
# print options to the user
# ask for the values
# call the function

def add(a,b):
    answer = a + b
    print(str(a)+" + "+str(b)+" = "+str(answer))

def sub(a,b):
    answer = a - b
    print(str(a)+" - "+str(b)+" = "+str(answer))
    
def mul(a,b):
    answer = a * b
    print(str(a)+" * "+str(b)+" = "+str(answer))
    
def div(a,b):
    answer = a / b
    print(str(a)+" / "+str(b)+" = "+str(answer))
    
print('A. Addition')
print('B. Subtraction')
print('C. Multiplication')
print('D. Division')
print('E. Exit')

<<<<<<< HEAD
choice = input('Enter your choice from A to E:')
=======
choice = input('Enter your choice:')
>>>>>>> refs/remotes/origin/main

# use a if else statments to continue the program until the user wants to exit
if choice == 'a' or choice =='A':
     print('Addition')
     a = int(input('First number: '))
     b = int(input('Second number: '))
     add(a,b)
     
elif choice == 'b' or choice =='B':
     print('Subtraction')
     a = int(input('First number: '))
     b = int(input('Second number: '))
     sub(a,b)

elif choice == 'c' or choice =='C':
     print('Multiplication')
     a = int(input('First number: '))
     b = int(input('Second number: '))
     mul(a,b)
     
elif choice == 'd' or choice =='D':
     print('Division')
     a = int(input('First number: '))
     b = int(input('Second number: '))
     div(a,b)
     
elif choice == 'e' or choice =='E':
     print('Goodbye!')
     quit()
     