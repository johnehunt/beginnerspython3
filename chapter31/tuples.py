class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person(' + self._name + ', ' + str(self._age) + ')'


tup1 = (1, 3, 5, 7)
print('tup1[0]:\t', tup1[0])
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

print('tup1[1:3]:\t', tup1[1:3])
print('tup1[:3]:\t', tup1[:3])
print('tup1[1:]:\t', tup1[1:])

print('tup1[::-1]:\t', tup1[::-1])

print('len(tup1):\t', len(tup1))

tup2 = (1, 'John', Person('Phoebe', 21), True, -23.45)
print(tup2)


tup3 = ('apple', 'pear', 'orange', 'plum', 'apple')
for x in tup3:
  print(x)

print(tup3.count('apple'))
print(tup3.index('pear'))

if 'orange' in tup3:
    print('orange is in the Tuple')

tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)
