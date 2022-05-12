def appendsums(lst): 
    """ 
    Repeatedly append the sum of the current last three elements 
    of lst to lst. 
    """
    sum_last_3 = 0
    for num in range(25):
        sum_last_3 = lst[-1] + lst[-2] + lst[-3]
        lst.append(sum_last_3)
        
    return lst
        
    
    
    

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]