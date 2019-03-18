def gen_numbers():
    yield 1
    yield 2
    yield 3


for i in gen_numbers():
    print(i)


def gen_numbers2():
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')


for i in gen_numbers2():
    print(i)


def evens_up_to(limit):
    value = 0
    while value <= limit:
        yield value
        value += 2


for i in evens_up_to(6):
    print(i, end=', ')

for i in evens_up_to(4):
    print('i:', i)

    for j in evens_up_to(6):
        print('j:', j, end=', ')

    print('')

evens = evens_up_to(4)
print(next(evens), end=', ')
print(next(evens), end=', ')
print(next(evens))
