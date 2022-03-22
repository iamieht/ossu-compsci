def iterPower(base, exp):
    '''
    base: float or int
    exp: int >= 0
    returns: num (base**exp)
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1

    return result

# Test Cases
print(iterPower(-3.77, 0))  #1.0000
print(iterPower(-4.97, 6)) #15070.8703
print(iterPower(9.78, 7)) #8557994.1152
print(iterPower(-0.74, 9)) #-0.0665
print(iterPower(-6.38, 9)) #-17514030.7747
print(iterPower(4.24, 0)) #1.0000
print(iterPower(0.04, 1)) #0.0400
print(iterPower(9.11, 0)) #1.0000