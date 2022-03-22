def fib(x):
    '''
    x: int >=0
    returns Fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)