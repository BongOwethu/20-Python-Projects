def main():
    print('This progaram convers US dollars to Pound Sterling (0_0)'+'\n')
    
    dollars = eval(input('Enter amount in dollars: '))
    
    pounds = convert_to_pounds(dollars)
    
    print('That is', pounds, 'pounds.') 
    
convert_to_pounds = lambda dollars: dollars * 0.82 

main()
    
  