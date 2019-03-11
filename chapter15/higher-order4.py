def make_checker(s):
    if s == 'even':
        return lambda n: n % 2 == 0
    elif s == 'positive':
        return lambda n: n >= 0
    elif s == 'negative':
        return lambda n: n < 0
    else:
        raise ValueError('Unknown request')


f1 = make_checker('even')
f2 = make_checker('positive')
f3 = make_checker('negative')
print(f1(3))
print(f2(3))
print(f3(3))


def make_function():
    def adder(x, y):
        return x + y

    return adder


f1 = make_function()
print(f1(3, 2))
print(f1(3, 3))
print(f1(3, 1))
