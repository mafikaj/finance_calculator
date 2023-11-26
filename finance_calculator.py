import math

# Display menu options for the user
print("investment: to calculate the amount of interest you'll earn on your investment: \n1")
print("bond: to calculate the amount you'll have to pay on a home loan: \n2")

# Prompt the user to choose between 'investment' and 'bond'
investment_type = input("Select either 'investment' or 'bond' to proceed: \n")

# For Investments, provide options for 'simple interest' and 'compound interest'
if investment_type.lower() == 'investment':
    principal_amount = float(
        input("Enter the amount the user is depositing: \n"))
    interest_rate_percentage = float(
        input("Enter the interest rate as a percentage: \n"))
    interest_rate = interest_rate_percentage / 100
    investment_period_years = float(
        input("Enter the number of years the user is planning to invest: \n"))

    print("Please select the type of interest between 'simple interest' or 'compound interest: \n")
    interest_choice = input(
        "Enter the interest: 'simple interest' or compound interest \n")

    total_amount = 0
    if interest_choice == 'simple interest':
        # Calculate total amount using the simple interest formula
        total_amount = principal_amount * \
            (1 + interest_rate * investment_period_years)
        print("The total amount after interest has been paid:",
              round(total_amount, 2))

    else:
        if interest_choice == 'compound interest':
            # Calculate total amount using the compound interest formula
            total_amount = principal_amount * \
                math.pow((1 + interest_rate), investment_period_years)
            print("The total amount after the interest has been paid:",
                  round(total_amount, 2))

# For 'bond', calculate the monthly repayment amount
elif investment_type.lower() == 'bond':
    present_value_of_house = float(
        input("Enter the current value of the house: \n"))
    interest_rate_percentage = float(
        input("Enter the current value of interest rate: \n"))
    interest_rate = interest_rate_percentage / 100
    monthly_interest_rate = interest_rate / 12

    repayment_period_months = float(
        input("Enter the number of months intended to pay for the bond: \n"))
    monthly_repayment_amount = (monthly_interest_rate * present_value_of_house) / \
        (1 - (1 + monthly_interest_rate)**(-repayment_period_months))
    print("The amount the user will pay each month:",
          round(monthly_repayment_amount, 2))

else:
    print("Invalid Entry")
