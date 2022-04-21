def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)