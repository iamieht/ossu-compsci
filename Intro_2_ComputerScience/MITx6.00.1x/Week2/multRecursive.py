def mult_recursive(a, b):
    if b == 1:
        return a
    else:
        return  a + mult_recursive(a, b-1)