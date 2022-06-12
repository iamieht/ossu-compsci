"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._current_cookies = 0.0
        self._total_cookies = 0.0
        self._cps = 1.0
        self._time = 0.0
        self._item = None
        self._item_price = 0.0
        self._history = [(self._time, self._item, 
                          self._item_price, 
                          self._total_cookies)]
        
    def __str__(self):
        """
        Return human readable state
        """
        _string = "Time: " + str(self._time)\
                + "\nCurrent cookies: " + str(self._current_cookies)\
                + "\nCPS: " + str(self._cps)\
                + "\nTotal cookies: " + str(self._total_cookies)

        return _string
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies > 0 and cookies > self._current_cookies:
            return math.ceil((cookies - self._current_cookies)/self._cps)
        else:
            return 0.0
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._time += time
            self._current_cookies += self._cps * time
            self._total_cookies += self._cps * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._item = item_name
            self._item_price = cost
            self._cps += additional_cps
            self._history.append((self._time, self._item, 
                                  self._item_price, 
                                  self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    build_object = build_info.clone()
    simulation = ClickerState()
    while simulation.get_time() <= duration:
        time_left = duration - simulation.get_time()
        next_item_to_buy = strategy(simulation.get_cookies(),
                                    simulation.get_cps(),
                                    simulation.get_history(),
                                    time_left, build_object)
        if next_item_to_buy == None:
            break
        elif simulation.time_until(build_object.get_cost(next_item_to_buy)) > time_left:
            break
        else:
            simulation.wait(simulation.time_until(build_object.get_cost(next_item_to_buy)))
            simulation.buy_item(next_item_to_buy,
                                build_object.get_cost(next_item_to_buy),
                                build_object.get_cps(next_item_to_buy))
            build_object.update_item(next_item_to_buy)
    simulation.wait(time_left)
    return simulation

def item_price_dict(build_info):
    """
    Returns dictionary with item name and it's price.
    """
    all_items = build_info.build_items()
    costs = map(build_info.get_cost, all_items)
    items_costs_tuple = zip(all_items, costs)
    items_costs_dict = dict((item_name, cost) for (item_name, cost) in items_costs_tuple)
    return items_costs_dict

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    items = item_price_dict(build_info)
    minimum = min(zip(items.values(), items.keys()))
    if minimum[0] > time_left:
        return None
    else:
        return minimum[1]

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    items = item_price_dict(build_info)
    items_in_time = {}
    for item, price in items.items():
        if price <= cookies + cps * time_left:
            items_in_time[item] = price
    if items_in_time:
        maximum = max(zip(items_in_time.values(), items_in_time.keys()))
        return maximum[1]
    else:
        return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    items = item_price_dict(build_info)
    items_in_time = {}
    for item, price in items.items():
        if price <= cookies + cps * time_left:
            items_in_time[item] = price
    best_increase = {}
    for item, price in items_in_time.items():
        best_increase[item] = build_info.get_cps(item) / price
    if best_increase:
        best_choice = max(zip(best_increase.values(), best_increase.keys()))
        return best_choice[1]
    else:
        return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state 

    # Plot total cookies over time
    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it
    # Also comment out "None" strategy in run function for the program to work correctly.

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()

#CodeSkulptor: https://py2.codeskulptor.org/#user49_keaJWZXsQu_11.py
    

