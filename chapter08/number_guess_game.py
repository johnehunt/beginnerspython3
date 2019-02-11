import random

print('Welcome to the number guess game')

# Initialise the number to be guessed
number_to_guess = random.randint(1,10)

# Initialise the number of tries the player has made
count_number_of_tries = 1

# Obtain their initial guess
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
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

    # Obtain their next guess and increment number of attempts
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1

# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries , 'goes to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was',
          number_to_guess)

print('Game Over')