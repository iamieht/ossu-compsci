"""
Example comparisons of growth rates
"""

import simpleplot

def f(n):
    """
    A test function
    """
    return 0.1 * n ** 3 + 20 * n

def g(n):
    """
    A test function
    """
    return n ** 3
    #return 20 * n ** 2
    #return .1 * n ** 4

def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    answer = []
    for index in range(10, plot_length):
        answer.append([index, fun1(index) / float(fun2(index))])
    simpleplot.plot_lines("Growth rate comparison", 300, 300, "n", "f(n)/g(n)", [answer])
    
# create an example plot    
make_plot(f, g, 100)

