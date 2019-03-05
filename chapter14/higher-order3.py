import math


def simple_tax_calculator(amount):
    return math.ceil(amount * 0.3)


def calculate_tax(salary, func):
    return func(salary)


print(calculate_tax(45000.0, simple_tax_calculator))
