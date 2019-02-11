import random

min = 1
max = 6

roll_again = 'y'

while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(min, max)
    print(dice1)
    dice2 = random.randint(min, max)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')
