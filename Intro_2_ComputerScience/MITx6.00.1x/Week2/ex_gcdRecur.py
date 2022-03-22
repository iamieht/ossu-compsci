def gcdRecur(a, b):
    '''
    a: int
    b: int
    returns the largest integer that divides each of them without remainder
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# Test Cases
print(gcdRecur(2, 12)) #2
print(gcdRecur(6, 12)) #6
print(gcdRecur(9, 12)) #3
print(gcdRecur(17, 12)) #1
print(gcdRecur(96, 256)) #32
print(gcdRecur(76, 247)) #19
print(gcdRecur(13, 20)) #1
print(gcdRecur(112, 98)) #14
print(gcdRecur(76, 100)) #4
print(gcdRecur(198, 306)) #18
print(gcdRecur(48, 18)) #6
print(gcdRecur(169, 117)) #13
print(gcdRecur(180, 10)) #10
print(gcdRecur(48, 92)) #4