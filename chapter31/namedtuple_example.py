from collections import namedtuple

# Creates a new tuple subclass called Person
Person = namedtuple('Person', ['age', 'gender', 'name'])

# Can use new subclass to create tuple-like objects
row1 = Person(age=22, gender='male', name='Gryff')
print(row1.age)

row2 = Person(age=22, gender='female', name='Phoebe')
print(row2.name)