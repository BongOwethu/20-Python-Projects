#collect email. from user 
#split the email using at @ and save the first part as the user name,the 2nd part will have the domial
#split domain using '.'

def main():
    
    while True:
        choice = input('Pleasse type in Yes to continue(y) or Exit (e):').lower()
        
        if choice == 'yes' or choice == 'y':
            email_input = input('Input your email adress: ')
            #Split the inputted email into user name,domain and extention
            (username, domain) = email_input.split('@')
            (domain, extension) = domain.split('.')
        
            print('Username: ', username)
            print('Domain: ', domain)
            print('Extention: ', extension+'\n')
        
        elif choice == 'exit' or choice == 'e':
            print('Goodbye!'+ '\n')
            quit()
        
        else:
            print('Invalid input. Please type in Yes to continue(y) or Exit (e). :(')
    
print('Welcom to the email slicer :)')
print()
main()
    
      
    
    
 