import math
# The programme displays 'investment and bond' on the menu bar
print("investment: to calculate the amount of interest you'll earn on your investment: \n1")
print("bond: to calculate the amount you'll have to paye on a home loan: \n2")

# The programme ask the user select 'investment" or 'bond' on the menu so as to proceed
investment_type = input("Select either 'investment' or 'bond' to proceed: \n") 

# For Investments, there are two types of investements that the user will choose from 'simple interest' and ' compound interest'
if investment_type.lower() == 'investment':
    deposit = float(input("Enter the amount the user is depositing: \n"))
    #interest entered by the user in then divided by 100 before using it in the formula
    interest = float(input("Enter the number as a percentage: \n"))
    interest_rate = interest/100 
    number_years = float(input("Enter the number of years the user is planning to invest: \n"))

    print("Please select the type of interest between ' simple interest' or 'compound interest: \n")
    interest_choice = input("Enter the interest: 'simple interest' or compound interest \n")
    
    # set total amount to zero
    # apply the elif statement to all the user to choose which type of interest will be suitable
    # simple interest is calculated using the formula [total_amount = deposit * (1 + interest_rate * number_years)]
    # comoound interest is calculated [ total_amount = deposit * math.pow((1 + interest_rate), number_years)]
    total_amount = 0
    if interest_choice == 'simple interest': 
        total_amount = deposit * (1 + interest_rate * number_years )
        print("The total amount after interest has been paid:", round(total_amount, 2))

    else:
        if interest_choice == 'compound interest':
            total_amount = deposit * math.pow((1 + interest_rate), number_years)
            print("The total amount after the interest has been paid:",round(total_amount, 2))

# if a user enters investmen type as 'bond"
# to calculate the bond we use the formula [total_amount = (current_interest_rate * value_of_house) / (1 + current_interest_rate)** (-number_of_months)]
elif investment_type.lower() == 'bond':  
    value_of_house = float(input("Enter the current value of the house: \n"))
    # interest entered by the user is divided by 100 and then devided by 12 so that it can be used on the formula
    interest = float(input("Enter the current value of interest rate: \n"))
    interest_rate = interest / 100
    current_interest_rate = interest_rate / 12

    number_of_months = float(input("Enter the number of months intended to pay for the bond: \n"))
    total_amount = (current_interest_rate * value_of_house) / (1 - (1 + current_interest_rate)** (-number_of_months))
    print("The amount the user will pay each month:",round(total_amount, 2))

else:
    print("Invalid Entry")