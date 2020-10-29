class Person:
    """ An example class to hold a persons name and age"""

    def __init__(self, name, age):
        print('init called with', name, age)
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        print('__new__ called')
        return super(Person, cls).__new__(cls)

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age < 20


p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

px = p1
print('id(p1):', id(p1))
print('id(px):', id(px))
print('id(p2):', id(p2))

print(p1)
print(px)
print(p2)

print(p1.name, 'is', p1.age)
print(p2.name, 'is', p2.age)

p3 = Person('Adam', 19)
print(p3)
p3.birthday()
print(p3)

pay = p2.calculate_pay(40)
print('Pay', p2.name, pay)
pay = p3.calculate_pay(40)
print('Pay', p3.name, pay)

print('-' * 20)
p1 = Person('John', 36)
print(p1)
print(p1.name, 'is', p1.age)
print('p1.is_teenager', p1.is_teenager())
p1.birthday()
print(p1)
p1.age = 18
print(p1)

print(p1.__doc__)
