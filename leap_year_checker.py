def is_leap_year(year):
    if year % 4 == 0: # use nested if loop to check leap year
        if year % 100 ==0 :
            if year % 400 == 0:
                print('Leap yaer (0_0)')
            else:
                print('Not Leap yaer (*_*)')  
        else:
            print('Leap yaer (0_0)')
    else:
        print('Not Leap yaer (*_*)')
        
is_leap_year(2009) # change ther leap year here can use theses years:2000,2020,2024