# Recursive functions


def factorial(n, depth=1):
    if n == 1: # The base case
        print('\t' * depth, 'Returning 1')
        return 1
    else: # The recursive part
        print('\t' * depth, 'Recursively calling factorial(', n - 1, ')')
        result = n * factorial(n - 1, depth + 1)
        print('\t' * depth, 'Returning:', result)
        return result


print('Calling factorial( 5 )')
print(factorial(5))

# Tail recursive example


def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n - 1, accumulator * n)


print(tail_factorial(5))
