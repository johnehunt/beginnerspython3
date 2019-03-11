def runcalc(x):
    x / 0


def print_value(i, list):
    print(list[i])


def print_alt_value(i, list):
    if i > len(list):
        raise ValueError('Invalid length ' + str(i))
    print(list[i])


def my_function(x, y):
    print('my_function in')
    result = x / y
    print('my_function out')
    return result


def f2():
    print('f2 in')
    function_bang()
    print('f2 out')


def function_bang():
    print('function_bang in')
    raise ValueError('Bang!')
    print('function_bang out')


class InvalidAgeException(Exception):
    """ Valid Ages must be between 0 and 120 """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'InvalidAgeException(' + str(self.value) + ')'


class DivideByYWhenZeroException(Exception):
    """ Sample Exception class"""


def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        raise DivideByYWhenZeroException from e


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method(', value, ')')
        if isinstance(value, int) & (value > 0 & value < 120):
            self._age = value
        else:
            raise InvalidAgeException(value)

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + self._age


divide(6, 0)

try:
    p = Person('John', 21)
    p.age = -1
except InvalidAgeException as e:
    print(e)

print('Starting')
try:
    print('Before my_function')
    my_function(6, 2)
    print('After my_function')
except ZeroDivisionError as exp:
    print('oops')
else:
    print('All OK')

print('Done')

try:
    my_function(6, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
finally:
    print('Always runs')

try:
    function_bang()
except ValueError as ve:
    print(ve)
    raise

l = [1, 2, 3, 4]
try:
    print_alt_value(7, l)
except Exception as e:
    print(e)

l = [1, 2, 3, 4]
try:
    print_value(2, l)
    print_value(3, l)
except IndexError as e:
    print('Exception: ', e)
else:
    print('All OK')
finally:
    print('Always runs')

print(divide(3, 0))
