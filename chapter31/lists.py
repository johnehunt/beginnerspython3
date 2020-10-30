class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person(' + self._name + ', ' + str(self._age) + ')'


list1 = ['John', 'Paul', 'George', 'Ringo']
list2 = [4]
list3 = []
list4 = [1, "two", 3, 'four']
list5 = [[2, 3], [6, 8]]

print(type(list5))
print(list1, ': ', len(list1))
print(list2, ': ', len(list2))
print(list3, ': ', len(list3))
print(list4, ': ', len(list4))
print(list5, ': ', len(list5))

print('list1[1]:', list1[1])
print('list1[-1]:', list1[-1])
print('list1[1:3]:', list1[1:3])
print('list[:3]:', list1[:3])
print('list[1:]:', list1[1:])

# Check for membership
if 'Pete' in list1:
    print('Pete in the list')
else:
    print('Pete not in the list')

list1.append('Pete')
print(list1)
list1.extend(['Albert', 'Bob'])
print(list1)
list1 += ['Ginger', 'Sporty']
print(list1)
list1.insert(2, 7)
print(list1)

list6 = ['Once', 'Upon', 'a', 'Time']
print(list6)
print(list6.pop(2))
print(list6)
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6)
print(list6.pop())
print(list6)
list6.remove('Upon')
print(list6)

list7 = [2, 3, 6, 8]
print(list7.index(8))
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6.index('a'))

print('-' * 50)
l1 = [1, 43.5, Person('Phoebe', 21), True]
l2 = ['apple', 'orange', 31]
root_list = ['John', l1, l2, 'Denise']
print(root_list)

t1 = (1, 'John', 34.5)
ll1 = ['Smith', 'Jones']
ll2 = [t1, ll1]
t2 = (ll2, 'apple')
print(t2)

a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)

another_list = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_list)
another_list.remove('Robbie')
print(another_list)

my_list = ['A', 'B', 'C', 'D', 'E']
print(my_list)
del my_list[2]
print(my_list)
my_list = ['A', 'B', 'C', 'D', 'E']
print(my_list)
del my_list[1:3]
print(my_list)
