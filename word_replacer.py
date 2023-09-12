def replace_word():
    str = 'Hi there, my name is Mandisa,hi hi hi hi!' #the word you are going to use to replace
    word_to_replace = input("Enter the word you want to replace: ") #get user input forreplacement
    new_word = input("Enter the new word: ") #new word replaced
    print(str.replace(word_to_replace,new_word)) # using the method replace in string to replace with new word
    
replace_word() #call function