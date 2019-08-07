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
        print('In set_age method')
        if isinstance(value, int) & value > 0 & value < 120:
            self._age = value

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


person = Person('John', 54)
print(person)
print(person.age)
print(person.name)
person.age = 21
print(person)
