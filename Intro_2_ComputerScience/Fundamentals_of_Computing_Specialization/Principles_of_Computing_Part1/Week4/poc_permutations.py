"""
Function to generate permutations of outcomes
Repetition of outcomes not allowed
"""

def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if item in seq:
                    continue
                else:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans



def run_example():

    # example for digits
    
    #outcome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcome = ["Red", "Green", "Blue"]
    outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    length = 3
    permtutations = gen_permutations(outcome, length)
    print "Computed", len(permtutations), "permutations of length", str(length)
    print "Permutations were", permtutations

    

run_example()



#######################################
# Example output below
#
#Computed 90 permutations of length 2
#Permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])#
#
#Computed 6 permutations of length 2
#Permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green')])
#
#Computed 210 permutations of length 3
#Permutations were set([('Sunday', 'Monday', 'Tuesday'), ('Sunday', 'Monday', 'Wednesday'), ('Sunday', 'Monday', 'Thursday'), ('Sunday', 'Monday', 'Friday'), ('Sunday', 'Monday', 'Saturday'), ('Sunday', 'Tuesday', 'Monday'), ('Sunday', 'Tuesday', 'Wednesday'), ('Sunday', 'Tuesday', 'Thursday'), ('Sunday', 'Tuesday', 'Friday'), ('Sunday', 'Tuesday', 'Saturday'), ('Sunday', 'Wednesday', 'Monday'), ('Sunday', 'Wednesday', 'Tuesday'), ('Sunday', 'Wednesday', 'Thursday'), ('Sunday', 'Wednesday', 'Friday'), ('Sunday', 'Wednesday', 'Saturday'), ('Sunday', 'Thursday', 'Monday'), ('Sunday', 'Thursday', 'Tuesday'), ('Sunday', 'Thursday', 'Wednesday'), ('Sunday', 'Thursday', 'Friday'), ('Sunday', 'Thursday', 'Saturday'), ('Sunday', 'Friday', 'Monday'), ('Sunday', 'Friday', 'Tuesday'), ('Sunday', 'Friday', 'Wednesday'), ('Sunday', 'Friday', 'Thursday'), ('Sunday', 'Friday', 'Saturday'), ('Sunday', 'Saturday', 'Monday'), ('Sunday', 'Saturday', 'Tuesday'), ('Sunday', 'Saturday', 'Wednesday'), ('Sunday', 'Saturday', 'Thursday'), ('Sunday', 'Saturday', 'Friday'), ('Monday', 'Sunday', 'Tuesday'), ('Monday', 'Sunday', 'Wednesday'), ('Monday', 'Sunday', 'Thursday'), ('Monday', 'Sunday', 'Friday'), ('Monday', 'Sunday', 'Saturday'), ('Monday', 'Tuesday', 'Sunday'), ('Monday', 'Tuesday', 'Wednesday'), ('Monday', 'Tuesday', 'Thursday'), ('Monday', 'Tuesday', 'Friday'), ('Monday', 'Tuesday', 'Saturday'), ('Monday', 'Wednesday', 'Sunday'), ('Monday', 'Wednesday', 'Tuesday'), ('Monday', 'Wednesday', 'Thursday'), ('Monday', 'Wednesday', 'Friday'), ('Monday', 'Wednesday', 'Saturday'), ('Monday', 'Thursday', 'Sunday'), ('Monday', 'Thursday', 'Tuesday'), ('Monday', 'Thursday', 'Wednesday'), ('Monday', 'Thursday', 'Friday'), ('Monday', 'Thursday', 'Saturday'), ('Monday', 'Friday', 'Sunday'), ('Monday', 'Friday', 'Tuesday'), ('Monday', 'Friday', 'Wednesday'), ('Monday', 'Friday', 'Thursday'), ('Monday', 'Friday', 'Saturday'), ('Monday', 'Saturday', 'Sunday'), ('Monday', 'Saturday', 'Tuesday'), ('Monday', 'Saturday', 'Wednesday'), ('Monday', 'Saturday', 'Thursday'), ('Monday', 'Saturday', 'Friday'), ('Tuesday', 'Sunday', 'Monday'), ('Tuesday', 'Sunday', 'Wednesday'), ('Tuesday', 'Sunday', 'Thursday'), ('Tuesday', 'Sunday', 'Friday'), ('Tuesday', 'Sunday', 'Saturday'), ('Tuesday', 'Monday', 'Sunday'), ('Tuesday', 'Monday', 'Wednesday'), ('Tuesday', 'Monday', 'Thursday'), ('Tuesday', 'Monday', 'Friday'), ('Tuesday', 'Monday', 'Saturday'), ('Tuesday', 'Wednesday', 'Sunday'), ('Tuesday', 'Wednesday', 'Monday'), ('Tuesday', 'Wednesday', 'Thursday'), ('Tuesday', 'Wednesday', 'Friday'), ('Tuesday', 'Wednesday', 'Saturday'), ('Tuesday', 'Thursday', 'Sunday'), ('Tuesday', 'Thursday', 'Monday'), ('Tuesday', 'Thursday', 'Wednesday'), ('Tuesday', 'Thursday', 'Friday'), ('Tuesday', 'Thursday', 'Saturday'), ('Tuesday', 'Friday', 'Sunday'), ('Tuesday', 'Friday', 'Monday'), ('Tuesday', 'Friday', 'Wednesday'), ('Tuesday', 'Friday', 'Thursday'), ('Tuesday', 'Friday', 'Saturday'), ('Tuesday', 'Saturday', 'Sunday'), ('Tuesday', 'Saturday', 'Monday'), ('Tuesday', 'Saturday', 'Wednesday'), ('Tuesday', 'Saturday', 'Thursday'), ('Tuesday', 'Saturday', 'Friday'), ('Wednesday', 'Sunday', 'Monday'), ('Wednesday', 'Sunday', 'Tuesday'), ('Wednesday', 'Sunday', 'Thursday'), ('Wednesday', 'Sunday', 'Friday'), ('Wednesday', 'Sunday', 'Saturday'), ('Wednesday', 'Monday', 'Sunday'), ('Wednesday', 'Monday', 'Tuesday'), ('Wednesday', 'Monday', 'Thursday'), ('Wednesday', 'Monday', 'Friday'), ('Wednesday', 'Monday', 'Saturday'), ('Wednesday', 'Tuesday', 'Sunday'), ('Wednesday', 'Tuesday', 'Monday'), ('Wednesday', 'Tuesday', 'Thursday'), ('Wednesday', 'Tuesday', 'Friday'), ('Wednesday', 'Tuesday', 'Saturday'), ('Wednesday', 'Thursday', 'Sunday'), ('Wednesday', 'Thursday', 'Monday'), ('Wednesday', 'Thursday', 'Tuesday'), ('Wednesday', 'Thursday', 'Friday'), ('Wednesday', 'Thursday', 'Saturday'), ('Wednesday', 'Friday', 'Sunday'), ('Wednesday', 'Friday', 'Monday'), ('Wednesday', 'Friday', 'Tuesday'), ('Wednesday', 'Friday', 'Thursday'), ('Wednesday', 'Friday', 'Saturday'), ('Wednesday', 'Saturday', 'Sunday'), ('Wednesday', 'Saturday', 'Monday'), ('Wednesday', 'Saturday', 'Tuesday'), ('Wednesday', 'Saturday', 'Thursday'), ('Wednesday', 'Saturday', 'Friday'), ('Thursday', 'Sunday', 'Monday'), ('Thursday', 'Sunday', 'Tuesday'), ('Thursday', 'Sunday', 'Wednesday'), ('Thursday', 'Sunday', 'Friday'), ('Thursday', 'Sunday', 'Saturday'), ('Thursday', 'Monday', 'Sunday'), ('Thursday', 'Monday', 'Tuesday'), ('Thursday', 'Monday', 'Wednesday'), ('Thursday', 'Monday', 'Friday'), ('Thursday', 'Monday', 'Saturday'), ('Thursday', 'Tuesday', 'Sunday'), ('Thursday', 'Tuesday', 'Monday'), ('Thursday', 'Tuesday', 'Wednesday'), ('Thursday', 'Tuesday', 'Friday'), ('Thursday', 'Tuesday', 'Saturday'), ('Thursday', 'Wednesday', 'Sunday'), ('Thursday', 'Wednesday', 'Monday'), ('Thursday', 'Wednesday', 'Tuesday'), ('Thursday', 'Wednesday', 'Friday'), ('Thursday', 'Wednesday', 'Saturday'), ('Thursday', 'Friday', 'Sunday'), ('Thursday', 'Friday', 'Monday'), ('Thursday', 'Friday', 'Tuesday'), ('Thursday', 'Friday', 'Wednesday'), ('Thursday', 'Friday', 'Saturday'), ('Thursday', 'Saturday', 'Sunday'), ('Thursday', 'Saturday', 'Monday'), ('Thursday', 'Saturday', 'Tuesday'), ('Thursday', 'Saturday', 'Wednesday'), ('Thursday', 'Saturday', 'Friday'), ('Friday', 'Sunday', 'Monday'), ('Friday', 'Sunday', 'Tuesday'), ('Friday', 'Sunday', 'Wednesday'), ('Friday', 'Sunday', 'Thursday'), ('Friday', 'Sunday', 'Saturday'), ('Friday', 'Monday', 'Sunday'), ('Friday', 'Monday', 'Tuesday'), ('Friday', 'Monday', 'Wednesday'), ('Friday', 'Monday', 'Thursday'), ('Friday', 'Monday', 'Saturday'), ('Friday', 'Tuesday', 'Sunday'), ('Friday', 'Tuesday', 'Monday'), ('Friday', 'Tuesday', 'Wednesday'), ('Friday', 'Tuesday', 'Thursday'), ('Friday', 'Tuesday', 'Saturday'), ('Friday', 'Wednesday', 'Sunday'), ('Friday', 'Wednesday', 'Monday'), ('Friday', 'Wednesday', 'Tuesday'), ('Friday', 'Wednesday', 'Thursday'), ('Friday', 'Wednesday', 'Saturday'), ('Friday', 'Thursday', 'Sunday'), ('Friday', 'Thursday', 'Monday'), ('Friday', 'Thursday', 'Tuesday'), ('Friday', 'Thursday', 'Wednesday'), ('Friday', 'Thursday', 'Saturday'), ('Friday', 'Saturday', 'Sunday'), ('Friday', 'Saturday', 'Monday'), ('Friday', 'Saturday', 'Tuesday'), ('Friday', 'Saturday', 'Wednesday'), ('Friday', 'Saturday', 'Thursday'), ('Saturday', 'Sunday', 'Monday'), ('Saturday', 'Sunday', 'Tuesday'), ('Saturday', 'Sunday', 'Wednesday'), ('Saturday', 'Sunday', 'Thursday'), ('Saturday', 'Sunday', 'Friday'), ('Saturday', 'Monday', 'Sunday'), ('Saturday', 'Monday', 'Tuesday'), ('Saturday', 'Monday', 'Wednesday'), ('Saturday', 'Monday', 'Thursday'), ('Saturday', 'Monday', 'Friday'), ('Saturday', 'Tuesday', 'Sunday'), ('Saturday', 'Tuesday', 'Monday'), ('Saturday', 'Tuesday', 'Wednesday'), ('Saturday', 'Tuesday', 'Thursday'), ('Saturday', 'Tuesday', 'Friday'), ('Saturday', 'Wednesday', 'Sunday'), ('Saturday', 'Wednesday', 'Monday'), ('Saturday', 'Wednesday', 'Tuesday'), ('Saturday', 'Wednesday', 'Thursday'), ('Saturday', 'Wednesday', 'Friday'), ('Saturday', 'Thursday', 'Sunday'), ('Saturday', 'Thursday', 'Monday'), ('Saturday', 'Thursday', 'Tuesday'), ('Saturday', 'Thursday', 'Wednesday'), ('Saturday', 'Thursday', 'Friday'), ('Saturday', 'Friday', 'Sunday'), ('Saturday', 'Friday', 'Monday'), ('Saturday', 'Friday', 'Tuesday'), ('Saturday', 'Friday', 'Wednesday'), ('Saturday', 'Friday', 'Thursday')])



## Final example for homework problem
#
outcome = set(["a", "b", "c", "d", "e", "f"])
#
permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print
print "Answer is", permutation_list[100]
