# Recursion

def sum_up_to(n):
    if n == 1:
        # base case
        return 1
    else:
        # recursive case
        return n + sum_up_to(n - 1)

print sum_up_to(1)
print sum_up_to(2)
print sum_up_to(10)
print sum_up_to(55)

print sum(range(56))

def is_palindrome(word):
    if len(word) < 2:
        # base case
        return True
    else:
        # recursive case
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])

print is_palindrome("a")
print is_palindrome("aa")
print is_palindrome("is")
print is_palindrome("madamimadam")
print is_palindrome("abcdefdcba")
