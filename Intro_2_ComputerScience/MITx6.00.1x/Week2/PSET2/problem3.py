'''
Problem 3 - Using Bisection Search to Make the Program Faster
'''
# Test Case 1
# balance = 320000
# annualInterestRate = 0.2
##Lowest Payment: 29157.09

# Test Case 2
balance = 999999
annualInterestRate = 0.18
##Lowest Payment: 90325.03

# Main Program
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLow = balance / 12
monthlyPaymentHigh = (balance * (1 + monthlyInterestRate)**12) / 12.0
minMonthlyPayment = (monthlyPaymentHigh + monthlyPaymentLow) / 2.0
updatedBalance = balance
epsilon = 0.01

while True:
    for month in range(1, 13):
        monthlyUnpaidBalance = round(updatedBalance - minMonthlyPayment,2)
        updatedBalance = round(monthlyUnpaidBalance + (monthlyInterestRate *    monthlyUnpaidBalance),2)
        
    if updatedBalance > 0 and updatedBalance - monthlyUnpaidBalance > epsilon:
        monthlyPaymentLow = minMonthlyPayment
        updatedBalance = balance
    elif updatedBalance < 0 and updatedBalance - monthlyUnpaidBalance < epsilon:
        monthlyPaymentHigh = minMonthlyPayment
        updatedBalance = balance
    else:
        print('Lowest Payment', minMonthlyPayment)
        break
    
    minMonthlyPayment = round((monthlyPaymentHigh + monthlyPaymentLow) / 2.0,2)

                    
