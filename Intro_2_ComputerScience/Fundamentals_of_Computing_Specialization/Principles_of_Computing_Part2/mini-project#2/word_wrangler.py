"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    duplicate_free_list = []
    none_list = [None]*1000

    for index in range(len(list1)):
        if none_list[list1[index]] == None:
            duplicate_free_list.append(list1[index])
            none_list[list1[index]] = list1[index]

    return duplicate_free_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    joined_list = []
    none_list = [None]*1000

    list1 = remove_duplicates(list1)
    list2 = remove_duplicates(list2)

    for index in range(len(list1)):
        none_list[list1[index]] = list1[index]

    for index in range(len(list2)):
        if none_list[list2[index]] == list2[index]:
            joined_list.append(list2[index])

    return joined_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    merge_result = []
    idx = 0

    while list1 != [] and list2 != []:
        if list1[idx] < list2[idx]:
            merge_result.append(list1[idx])
            list1 = list1[idx + 1:]
        else:
            merge_result.append(list2[idx])
            list2 = list2[idx + 1:]

    # there might be some elements remaining in left or right subarrays

    while list1 != []:
        merge_result.append(list1[idx])
        list1 = list1[idx + 1:]

    while list2 != []:
        merge_result.append(list2[idx])
        list2 = list2[idx + 1:]

    return merge_result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # base case: a list of non-zero elements are sorted by definition
    if len(list1) <= 1:
        return list1

    # split the arrays by the middle and assign the halfs to left and right respectively
    middle = len(list1) // 2
    left, right = list1[:middle], list1[middle:]

    # recursively sort both the halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the now sorted sub-arrays
    return merge(left, right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
# CodeSkulptor: https://py2.codeskulptor.org/#user49_6WcxQXHPiq_5.py
    
    