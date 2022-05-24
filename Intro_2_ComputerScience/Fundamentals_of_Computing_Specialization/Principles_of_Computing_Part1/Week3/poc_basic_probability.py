"""
Conducting multiple trials using random.randrange()
"""


import random
import simpleplot

EVEN_EVENT = set([2, 4, 6])

def roll_die(num_sides):
    """
    Simulate a trail corresponding to the roll of die 
    with specified number of sides
    """
    result = random.randrange(0, num_sides) + 1
    return result

def roll_test(num_sides, num_rolls):
    """
    Roll a die with num_sides num_rolls number of times
    """
    print "Roll six-sided die " + str(num_rolls) + " times"
    for _ in range(num_rolls):
        roll = roll_die(num_sides)
        print "Roll was", roll
        #print "Roll was even is", roll in EVEN_EVENT

#roll_test(6, 10)







    
    
# Test whether random.randrage simulates a fair die        
        
TRIAL_STRIDE = 1

def plot_fairness(side, num_sides, max_trials):
    """
    Plot the mathematical probability for an outcome vs.
    computed estimate
    """
    plot = []
    for num_trials in range(TRIAL_STRIDE, max_trials, TRIAL_STRIDE):
        side_count = 0
        for _ in range(num_trials):
            if roll_die(num_sides) == side:
                side_count += 1
        mathematical = 1.0 / num_sides
        computed = float(side_count) / num_trials
        plot.append([num_trials, mathematical - computed])
    simpleplot.plot_lines("Fairness test", 400, 300, 
               "number of rolls", "mathematical - computed", [plot])
        
# check the fairness of the die
plot_fairness(1, 6, 300)    
    
    
    
    
    
    
    
    
    
    