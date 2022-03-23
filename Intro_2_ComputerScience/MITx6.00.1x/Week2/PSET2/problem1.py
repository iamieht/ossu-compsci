'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy
'''
# Test Case 1:
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
## Remaining balance: 31.38

# Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
## Remaining balance: 361.61

# Main Program
monthlyInterestRate = annualInterestRate / 12.0

for month in range(1,13):
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print('Remaining balance:', round(balance, 2))