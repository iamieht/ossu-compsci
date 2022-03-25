def count7(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    elif N%10 == 7:
        return 1 + count7(N//10)
    else:
        return count7(N//10)
    
#Test Cases
print(count7(717)) #2
print(count7(1237123)) #1
print(count7(8989)) #0