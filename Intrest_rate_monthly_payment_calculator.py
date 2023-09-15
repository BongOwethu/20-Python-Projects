# collect the necessary inputs:
# principal(loan amount), apr(annual interest rate,years(amount of years needed to pay to pay loan back)
# calcuate the monthly payments
# display for user in rands 

def main():
    print('This is a monthly loan calculator (0_0) '+'\n')
    
    principal = float(input("Loan amount: "))
    apr = float(input("Annual interest rate: "))
    years = int(input("Amount of years: "))
    
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    
    print('The monthly payment for this loan is: R%.2f ' % monthly_payment  + '\n')
    
main()