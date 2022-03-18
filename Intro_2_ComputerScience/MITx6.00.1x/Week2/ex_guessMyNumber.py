'''
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
'''
low = 0
high = 100
secretNumber = (high + low)//2
print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number ' + str(secretNumber) + '?')
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if guess == 'c':
        print('Game over. Your secret number was:', secretNumber)
        break
    elif guess == 'h':
        high = secretNumber
    elif guess == 'l':
        low = secretNumber
    else:
        print('Sorry, I did not understand your input.')
    
    secretNumber = (high + low)//2
