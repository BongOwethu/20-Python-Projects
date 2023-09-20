# have a python dictionary that has a key value pair that represents a word and it;s definition
# get user input from the user,check if input is a word
# check if word is in the dictionary
# print the definition

import PyDictionary # install using pip install PyDictionary

dictionary = PyDictionary{}

while True:
    word = input('Enter a word (9_9) or space to exit: ')
    if word == '':
        break
    
    print(dictionary.meaning(word))