import math


# Function of decorative line for better output legibility
def line():
    print('-' * 88)


# Function for validating only two types of input
def input_check(a, b):
    while True:
        option = input(f'Enter either \'{a}\' or \'{b}\' calculation to proceed: \t').lower()
        if option == a or option == b:
            return option
        else:
            print(f'Please enter only \'{a}\' or \'{b}\' ')


# Function for validating numerical input
def number_check():   
    while True:    
        try:
            x = input(':\t\t')
            x = int(x)
            return x
        except ValueError:
            print("Invalid entry, please enter only whole digit", end='')

            
# Function of aggregate earned on simple rate investment
def simple_interest(x, y, z):
    a = round(x*(1 + y * z), 2)
    return a


# Function of aggregate earned on compound rate investment
def compound_interest(x, y, z):
    a = round(x * math.pow((1 + y), z), 2)
    return a


# Function of calculating monthly loan repayment
def repayment(x, y, z):
    a = round((y * x)/(1 - (1 + y) ** (-z)), 2)
    return a


# Main menu of the calculator    
line()
print('investment \t - to calculate the amount of interest you\'ll earn on your investment')
print('bond \t\t - to calculate the amount of interest you\'ll have to pay on a home loan \n')

# User selects only either investment or bond
calculator = input_check('investment', 'bond')
line()

# Investment
if calculator == 'investment':
    print('The principal amount (£)', end='')  # User inputs total amount of investment & numer_check validates the integer
    P = number_check()
    print('The annual interest rate (%)', end='')  # User inputs interest rate & number_check validates the integer
    r = number_check()/100
    print('The period involved (years)', end='')  # User inputs years of investment & number_check validates the integer
    t = number_check() 

    # User selects only either simple or compound calculation
    investment_option = input_check('simple', 'compound')

    if investment_option == 'simple':
        print(f'Simple interest: The total amount after {t} years:\t\t', end='')  # Define simple_interest function calculates the amount & outputs result
        print(simple_interest(P, r, t))
        line()
    elif investment_option == 'compound':
        print(f'Compound interest: The total amount after {t} years:\t\t', end='')  # Define compound_interest function calculates the amount & outputs the result
        print(compound_interest(P, r, t))
        line()
# Bond        
elif calculator == 'bond':
    print('Present value of the house (£)', end='')  # User inputs total value of the house & number_check validates the input
    P = number_check()
    print('The annual interest rate (%)', end='')  # User inputs interest rate & number_check validates the input
    i = ((number_check())/100)/12
    print('The repayment period (months)', end='')          # User inputs number of repayment months & number_check validates the input
    n = number_check()
    print('Your monthly repayment:\t\t', end='')            # Define repayment function calculates the monthly repayment amount & outputs the result
    print(repayment(P, i, n))
    line()

# Suggestive successive instruction is printed out
print('Please restart to begin new calculation')
