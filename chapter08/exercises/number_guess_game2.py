# Provide a solution to exercise 3 - allow the user to play again
import random

print('Welcome to the number guess game')

# Exercise 3 - provide a play_again flag
continue_to_play = True
while continue_to_play:

    # Initialise the number to be guessed
    number_to_guess = random.randint(1, 10)

    # Initialise the number of tries the player has made
    count_number_of_tries = 1

    # Obtain their initial guess
    guess = int(input('Please guess a number between 1 and 10: '))
    while number_to_guess != guess:

        # Exercise 1 - Provide a cheat mode if the user enters -1
        if guess == -1:
            print('Cheat mode, number to guess is: ', number_to_guess)
            guess = int(input('Please guess again: '))
            continue  # this will jump the game play past the rest of the loop

        print('Sorry wrong number')

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if count_number_of_tries == 4:
            break
        elif guess < number_to_guess:
            print('Your guess was lower than the number')
        else:
            print('Your guess was higher than the number')

        if guess == guess + 1 or guess == guess - 1:
            print('Your guess was within 1 of the number')

        # Exercise 2 - notify the user if they are within 1 of the actual number
        if guess + 1 == number_to_guess or guess - 1 == number_to_guess:
            print('Your guess was within 1 of the number')

        # Exercise 2 - Obtain their next guess and increment number of attempts
        guess = int(input('Please guess again: '))
        count_number_of_tries += 1

    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print('You took', count_number_of_tries, 'goes to complete the game')
    else:
        print("Sorry - you loose")
        print('The number you needed to guess was',
              number_to_guess)

    # note use of lower to ensure that if the user enters 'n' or 'N' we take it as No
    play_again = input('Do you want to play again (y/n)? ')
    if play_again.lower() == 'n':
        continue_to_play = False

print('Game Over')
