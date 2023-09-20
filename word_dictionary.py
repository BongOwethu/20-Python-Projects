# have a python dictionary that has a key value pair that represents a word and it;s definition
# get user input from the user,check if input is a word
# check if word is in the dictionary
# print the definition

def main():
    word_dictionary ={
        'hi':'a way of greeting',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in space',
    }
    
    while True:
        word = input('Enter a word or space to exit: ')
        if word == '':
            break
        if word in word_dictionary:
            print(word, ':', word_dictionary[word])
            
main()