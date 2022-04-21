def liner_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found