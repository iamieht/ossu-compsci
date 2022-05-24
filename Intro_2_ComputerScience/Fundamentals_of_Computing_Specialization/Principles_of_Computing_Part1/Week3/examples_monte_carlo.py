"""
Monte Carlo simulation to compute the expectation that 
you will get three-of-a-kind when rolling 5 dice.
"""

import random
import math
import simpleplot
import codeskulptor

codeskulptor.set_timeout(30)

def compute_trial():
    """
    Trial: roll five six-sided dice
    """
    return [random.randrange(1, 7) for dummy in range(5)]

def check_event(dice):
    """
    Event: rolled three-of-a-kind
    """
    for die in set(dice):
        if dice.count(die) == 3:
            return True
    return False

def simulation_step():
    """
    One step of the Monte Carlo simulation.
    """
    result = compute_trial()
    event = check_event(result)
    return event

def monte_carlo(ntrials):
    """
    Basic Monte Carlo simulation.
    """
    events = 0
    for dummy in range(ntrials):
        event = simulation_step()
        if event:
            events += 1

    # Return expectation of the event
    return float(events) / float(ntrials)

def run():
    """
    Run Monte Carlo simulations with different numbers 
    of trials to estimate the expectation that you will 
    get 3-of-a-kind when rolling 5 dice.
    
    Actual probability of 3-of-a-kind: .1929
    """
    trial_sizes = [10, 100, 1000, 10000, 100000]
    estimates = []
    for ntrials in trial_sizes:
        estimates.append((ntrials, monte_carlo(ntrials)))
    for ntrials, est in estimates:
        print ntrials, ":", est
        
    log_estimates = [(math.log(ntrials, 10), est)
                     for ntrials, est in estimates]
    simpleplot.plot_bars("3-of-a-Kind", 400, 300, 
                         "Log(Trials)", "Expectation", 
                         [log_estimates])
        
run()

