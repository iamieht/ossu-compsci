def fourthPower(x):
    '''
    x: int or float
    returns the value raised to the fourth power
    '''
    def square(x):
        '''
        x: int or float
        returns the square of the number x
        '''
        return x*x
    
    return square(square(x))

# Test Cases
print(fourthPower(-2.49)) #38.4412
print(fourthPower(-9.77)) #9111.2561
print(fourthPower(-3.82)) #212.9381
print(fourthPower(0.03)) #0.0000