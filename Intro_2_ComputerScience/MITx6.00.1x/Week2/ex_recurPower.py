def recurPower(base, exp):
    '''
    base: float or int
    exp: int >= 0
    returns: num (base**exp)
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

# Test Cases
print(recurPower(3.11, 0)) #1.0000
print(recurPower(-5.11, 8)) #464908.1944
print(recurPower(-5.58, 10)) #29264559.3668
print(recurPower(2.78, 5)) #166.0443
print(recurPower(8.28, 2)) #68.5584
print(recurPower(-0.93, 1)) #-0.9300
print(recurPower(-3.78, 4)) #204.1584