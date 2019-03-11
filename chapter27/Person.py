# Example Illustrating Polymorphism


class Person:
    def eat(self): print('Person - Eat')

    def drink(self): print('Person - Drink')

    def sleep(self): print('Person - Sleep')


class Employee(Person):
    def eat(self): print('Employee - Eat')

    def drink(self): print('Employee - Drink')

    def sleep(self): print('Employee - Sleep')


class SalesPerson(Employee):
    def eat(self): print('SalesPerson - Eat')

    def drink(self): print('SalesPerson - Drink')


class Dog:
    def eat(self): print('Dog - Eat')

    def drink(self): print('Dog - Drink')

    def sleep(self): print('Dog - Sleep')


def night_out(p):
    p.eat()
    p.drink()
    p.sleep()


# Create instance sof each type
p = Person()
e = Employee()
s = SalesPerson()
d = Dog()

# Now use the function night_out
# with each type of object
print('-' * 25)
night_out(p)
print('-' * 25)
night_out(e)
print('-' * 25)
night_out(s)
print('-' * 25)
night_out(d)
