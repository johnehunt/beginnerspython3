number = input('Please input the number:')

if number.isnumeric():
    num = int(number)

    if num == 0:
        # Termination criteria
        print('0! factorial is 1')
    else:
        # Looping element
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(number + '! factorial is', str(factorial))

else:
    print('Not an integer number')
