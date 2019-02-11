def multiply(a, b):
    return a * b


print(multiply(2, 5))


def multby(func, num):
    return lambda y: func(num, y)


double = multby(multiply, 2)

triple = multby(multiply, 3)

print(double(5))
print(triple(5))
