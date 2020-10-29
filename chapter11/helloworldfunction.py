def print_msg():
    print('Hello World!')


print_msg()
print(type(print_msg))


def print_my_msg(msg):
    print(msg)


print_my_msg('Hello World')
print_my_msg('Good day')
print_my_msg('Welcome')
print_my_msg('Ola')


def square(n):
    return n * n


# Store result from square in a variable
result = square(4)
print(result)
# Send the result from square immediately to another function
print(square(5))
# Use the result returned form square in a conditional expression
if square(3) < 15:
    print('Still less than 15')


def swap(a, b):
    return b, a


a = 2
b = 3
x, y = swap(a, b)
print(x, ',', y)
print('----')

z = swap(a, b)
print(z)


def get_integer_input(message):
    """
    This function will display the message to the user
    and request that they input an integer.

    If the user enters something that is not a number
    then the input will be rejected
    and an error message will be displayed.

    The user will then be asked to try again."""

    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)

    return int(value_as_string)


age = get_integer_input('Please input your age: ')
print('age is', age)

print(get_integer_input.__doc__)


# Should really be make_a_list to follow Pythonic conventions
def makeAList(start, end):
    newList = list(range(start, end))
    return newList


def dictionary():
    return {'one': 1, 'two': 2}


list1 = makeAList(5, 10)
print(list1)

print(dictionary())

double = lambda i: i * i

print(double(10))
