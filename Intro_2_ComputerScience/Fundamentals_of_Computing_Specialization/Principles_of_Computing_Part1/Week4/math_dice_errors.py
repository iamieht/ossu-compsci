"""
Math dice game.

Roll two 12-sided dice and multiply them to get the target number.

Roll three 6-sided dice.  Combine them into a mathematical equation to
get the closest to the target as possible.

All equations are evaluated from left to right: (a op b) op c
"""

import random

### Math operators

def add(num1, num2):
    """
    Addition
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtraction
    """
    return num1 - num2

def mul(num1, num2):
    """
    Multiplication
    """
    return num1 * num2

def div(num1, num2):
    """
    Division
    """
    return float(num1) / num2

def power(num1, num2):
    """
    Exponentiation
    """
    return num1 ** num2


### Permutations and Sequences

def gen_permutations(elems):
    """
    Compute all permuations of elems.
    """
    stack = list(elems)
    results = [[stack.pop()]]
    while len(stack) != 0:
        item = stack.pop()
        new_results = []
        for perm in results:
            for i in range(len(perm)+1):
                new_results.append(perm[:i] + [item] + perm[i:])
        results = new_results
    return results

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """    
    ans = set([()])
    for dummy_idx in range(length + 1):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


### Dice operations

def roll(ndice, nsides):
    """
    Roll ndice with nsides.  Return a list of values.
    """
    return [random.randrange(1, nsides + 1) 
            for dummy in range(ndice)]

def product(dice):
    """
    Multiply all dice together.
    """
    result = 1
    for die in dice:
        result *= die
    return result


### Equation operations

def make_equations(ops, dice):
    """
    Make all equations
    """
    dice_orders = gen_permutations(dice)
    ops_orders = gen_all_sequences(ops.keys(), len(dice) - 1)
    results = []
    for dice_order in dice_orders:
        for ops_order in ops_orders:
            eqn = []
            for idx in range(len(ops_order)):
                eqn.append(dice_order[idx])
                eqn.append(ops_order[idx])
            eqn.append(dice_order[-1])
            val = evaluate(ops, eqn)
            eqn.append('=')
            eqn.append(val)     
            results.append(eqn)
    return results

def evaluate(ops, eqn):
    """
    Evaluate string equation of the form:

    [num, op, num, op, num]

    List can be of any length, but "num" elements must be numbers and
    "op" elements must be keys in ops dictionary.
    """
    val = eqn[0]
    idx = 1
    while idx < len(eqn):
        operation = eqn[idx]
        idx += 1
        num = eqn[idx]
        idx += 1
        val = ops[operation](val, num)
    return val

def find_closest(target, eqns):
    """
    Find equation that is closest to target value.
    """
    closest = [float('inf')]
    for eqn in eqns:
        if abs(target - eqn[-1]) < abs(closest[-1]):
            closest = eqn
    return closest

def string_equation(eqn):
    """
    Turn equation into human readable string.
    """
    streqn = "(" + str(eqn[0]) + " " + str(eqn[1])
    streqn += " " + str(eqn[2]) + ") " + str(eqn[3])
    streqn += " " + str(eqn[4]) + " " + str(eqn[5])
    streqn += " " + str(eqn[6])
    return streqn


### Game

def play():
    """
    Play round of Math Dice.
    """
    ops = {'+': add,
           '-': sub,
           '*': mul,
           '/': div,
           '**': power}

    targetdice = roll(2, 12)
    targetval = product(targetdice)
    dice = roll(3, 6)

    print "Target:", targetval, targetdice
    print "Dice:", dice

    eqns = make_equations(ops, dice)
    eqn = find_closest(targetval, eqns)

    print "Closest Equation:", string_equation(eqn)

play()
