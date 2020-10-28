from Person import Person

# Note must import reduce from functools module in Python 3
from functools import reduce

data = [1, 3, 5, 2, 7, 4, 10]
result = reduce(lambda total, value: total + value, data)
print(result)

def generate_total(running_total, value):
    return running_total + value

result = reduce(generate_total, data)
print(result)

data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
total_age = reduce(lambda running_total, person: running_total + person.age, data, 0)
average_age = total_age // len(data)
print('Average age:', average_age)

