'''
write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
'''
# Test Case 1:
#balance = 3329
#annualInterestRate = 0.2
##Lowest Payment: 310

# Test Case 2
balance = 4773
annualInterestRate = 0.2
##Lowest Payment: 440

# Main Program
monthlyInterestRate = annualInterestRate / 12.0
minMonthlyPayment = 10
updatedBalance = balance

while True:
    for month in range(1, 13):
        monthlyUnpaidBalance = round(updatedBalance - minMonthlyPayment,2)
        updatedBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),2)

    if updatedBalance <= 0:
        print('Lowest Payment:', minMonthlyPayment)
        break
    else:
        updatedBalance = balance
        minMonthlyPayment += 10

