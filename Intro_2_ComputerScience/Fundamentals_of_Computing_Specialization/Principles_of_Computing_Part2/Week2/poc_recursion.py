"""
Visualizing the execution of several 
simple recursive functions
"""

def collatz(num, count):
    """
    Given n, repeatedly perform n = f(n) where
    f(n) = n / 2 if n is even
    f(n) = 3 * n + 1 is n is odd
    Return number of iterations of this redution
    """
    if num == 1:
        return count
    elif (num % 2) == 0:
        return collatz(num / 2, count + 1)
    else:
        return collatz(3 * num + 1, count + 1)
    
print collatz(5, 0)


def quicksort(num_list):
    """
    Recursive O(n log(n)) sorting algorithm
    Takes a list of numbers
    Returns sorted list of same numbers
    """
    if num_list == []:
        return num_list
    else:
        pivot = num_list[0]
        lesser = [num for num in num_list if num < pivot]
        pivots = [num for num in num_list if num == pivot]
        greater = [num for num in num_list if num > pivot]
        return quicksort(lesser) + pivots + quicksort(greater)
    

#print quicksort([4, 5, 3, 1])




