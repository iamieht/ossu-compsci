def gcdIter(a, b):
    '''
    a: int
    b: int
    returns the largest integer that divides each of them without remainder
    '''
    smallest = min(a, b)
    gcd = 0
    while smallest >= 1:
        if (a % smallest) == 0 and (b % smallest) == 0:
            gcd = smallest
            break
        else:
            smallest -= 1 

    return gcd

# Test Cases
print(gcdIter(2, 12)) #2
print(gcdIter(6, 12)) #6
print(gcdIter(9, 12)) #3
print(gcdIter(17, 12)) #1
print(gcdIter(96, 256)) #32
print(gcdIter(76, 247)) #19
print(gcdIter(13, 20)) #1
print(gcdIter(112, 98)) #14
print(gcdIter(76, 100)) #4
print(gcdIter(198, 306)) #18
print(gcdIter(48, 18)) #6
print(gcdIter(169, 117)) #13
print(gcdIter(180, 10)) #10
print(gcdIter(48, 92)) #4