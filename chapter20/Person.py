class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)

    def __str__(self):
        return self.name + ' is ' + str(self.age)


class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def __str__(self):
        return super().__str__() + ' - id(' + str(self.id) + ')'


class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.5


print('Person')
p = Person('John', 54)
print(p)
p.birthday()
print(p.name)
print(p.age)
print('-' * 25)

print('Employee')
e = Employee('Denise', 51, 7468)
print(e)
e.birthday()
print(e.name)
print(e.age)
print(e.id)
print('e.calculate_pay(40):', e.calculate_pay(40))
print('-' * 25)

print('SalesPerson')
s = SalesPerson('Phoebe', 21, 4712, 'UK', 30000.0)
s.birthday()
print('s.calculate_pay(40):', s.calculate_pay(40))
print('s.bonus():', s.bonus())
