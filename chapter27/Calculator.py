from Quantity import Quantity


class Calculator:
    """ Simple Calculator class"""

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


class Distance:
    def __init__(self, d):
        self.value = d

    def __add__(self, other):
        return Distance(self.value + other.value)

    def __sub__(self, other):
        return Distance(self.value - other.value)

    def __str__(self):
        return 'Distance[' + str(self.value) + ']'


calc = Calculator()

print('calc.add(3, 4):', calc.add(3, 4))
print('calc.add(3, 4.5):', calc.add(3, 4.5))
print('calc.add(4.5, 6.2):', calc.add(4.5, 6.2))
print('calc.add(2.3, 7):', calc.add(2.3, 7))
print('calc.add(-1, 4):', calc.add(-1, 4))
print("calc.add('John', 'Hunt')", calc.add('John', 'Hunt'))

print('-' * 25)

q1 = Quantity(5)
q2 = Quantity(10)
print(calc.add(q1, q2))

print('-' * 25)

d1 = Distance(6)
d2 = Distance(3)
print(calc.add(d1, d2))
print(calc.subtract(d1, d2))
# print(calc.divide(d1, d2))
