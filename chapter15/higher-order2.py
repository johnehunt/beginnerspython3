def mult_by_two(num):
    return num * 2


def mult_by_5(num):
    return num * 5


def square(num):
    return num * num


def add_one(num):
    return num + 1


def apply(num, func):
    return func(num)


result = apply(10, mult_by_two)
print(result)

print(apply(10, mult_by_5))
print(apply(10, square))
print(apply(10, add_one))
print(apply(10, mult_by_two))
