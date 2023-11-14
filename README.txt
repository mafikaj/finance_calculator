# Finance Calculators

## Description

This Python program provides two financial calculators: an investment calculator and a home loan repayment calculator. Users can choose between these options and input relevant details to calculate the results.

## Table of Contents

1. [Usage](#usage)
    - [How to Run](#how-to-run)
2. [Calculators](#calculators)
    - [Investment Calculator](#investment-calculator)
    - [Home Loan Repayment Calculator](#home-loan-repayment-calculator)
3. [Example Usage](#example-usage)
4. [Things to Look Out For](#things-to-look-out-for)

## Usage

### How to Run

1. Make sure you have Python installed on your machine.
2. Download the `finance_calculators.py` file.
3. Open a terminal and navigate to the directory containing `finance_calculators.py`.
4. Run the program using the command: `python finance_calculators.py`.

## Calculators

### Investment Calculator

If the user selects 'investment', the program will prompt the user to input:
- The amount of money they are depositing.
- The interest rate (as a percentage).
- The number of years they plan on investing.
- Whether they want "simple" or "compound" interest.

The program will then calculate and display the total amount based on the chosen interest type.

### Home Loan Repayment Calculator

If the user selects 'bond', the program will prompt the user to input:
- The present value of the house.
- The interest rate.
- The number of months they plan to take to repay the bond.

The program will calculate and display the monthly repayment amount.

## Example Usage

### Investment Calculator

```bash
Select either 'investment' or 'bond' to proceed: investment

Enter the amount the user is depositing: 10000
Enter the number as a percentage: 8
Enter the number of years the user is planning to invest: 20
Enter the interest: 'simple interest' or 'compound interest: compound

Result:
The total amount after the interest has been paid: [calculated amount].
