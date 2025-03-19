# Game!
# Human player guess a number between 1 to n (specified by the user)
# the program will tell the user if the number they guess is too large, too small, or equal to the secret #
# we will randomly generate the secret #
# our program also needs to tell the user if their guess makes sense
# upper bound and a lower bound
# The user gets five tries

import random

print('Welcome to our Guessing Game! Please guess a number between the range of 1 to n, '
      'where you will specify n.')
print('After inputting the range, next you will enter your guess. if you want to stop playing '
      'enter a 0 or a negative number.')

upper_bound = int(input('Enter the end number of your guessing range: '))
lower_bound = 1

secret_number = random.randint(lower_bound, upper_bound)

users_guess = 0

count = 1

while users_guess != secret_number and count <= 5:
    users_guess = int(input("Enter your guess: "))
    if users_guess == 0 or users_guess <= 0:
        print('You have chosen to quit, Bye!')
        break
    elif users_guess > upper_bound:
        print("Your guess is not in the specified boundary!")
    elif users_guess < secret_number:
        print('That guess is too small!')
    elif users_guess > secret_number:
        print('That guess is too large!')
    else:
        print('Congrats! You guessed correctly!')
    count += 1
print('Thanks for playing!')