def evalQuadratic(a, b, c, x):
    '''
    a,b,c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b*x + c

# Test Cases
print(evalQuadratic(8.98, -2.24, 6.95, -3.89)) #151.5499
print(evalQuadratic(-4.38, 4.83, -9.3, -5.56)) #-171.5564
print(evalQuadratic(9.24, 8.29, -4.63, -3.28)) #67.5864
print(evalQuadratic(5.34, 6.35, -1.3, -8.49)) #329.6962
print(evalQuadratic(-0.59, 1.28, 3.47, -7.18)) #-36.1363