from Person import Person

data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

# Apply the lambda function to each element in the list
# using the map function
d1 = list(map(lambda i: i + 1, data))
print('d1', d1)


def add_one(i):
    return i + 1


# Apply the add_one function to each element in the
# list using the map function
d2 = list(map(add_one, data))
print('d2:', d2)

data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

result = list(map(lambda x, y: x + y, data1, data2))
print(result)

data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
ages = list(map(lambda p: p.age, data))
print(ages)
