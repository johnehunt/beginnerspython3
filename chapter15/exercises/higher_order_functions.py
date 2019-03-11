def my_higher_order_function(arg, func):
    return func(arg)


def double(num):
    return num * num


def triple(num):
    return num * num * num


def square_root(num):
    return num ** 0.5


def is_prime(num):
    """Returns True if the number is prime else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def is_integer(string):
    return string.isnumeric()


def is_letter(string):
    return string.isalpha()


print(my_higher_order_function(2, double))
print(my_higher_order_function(2, triple))
print(my_higher_order_function(16, square_root))
print(my_higher_order_function(2, is_prime))
print(my_higher_order_function(4, is_prime))
print(my_higher_order_function('2', is_integer))
print(my_higher_order_function('A', is_integer))
print(my_higher_order_function('A', is_letter))
print(my_higher_order_function('1', is_letter))
