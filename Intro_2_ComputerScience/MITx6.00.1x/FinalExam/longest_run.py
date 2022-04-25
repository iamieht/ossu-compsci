def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    decreasing = 0
    increasing = 0
    maxcount = 0
    result = 0

    for element in range(len(L) - 1):
        if (L[element] <= L[element + 1]):
            decreasing += 1
            if decreasing > maxcount:
                maxcount = decreasing
                result = element + 1
        else:
            decreasing = 0

        if (L[element] >= L[element + 1]):
            increasing += 1            
            if increasing > maxcount:
                maxcount = increasing
                result = element + 1
        else:
            increasing = 0
        
    first = result - maxcount
    summ = sum(L[first:result + 1])
    return summ


#Test Cases
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(longest_run(L))
L2 = [5, 4, 10]
print(longest_run(L2))