def logger(func):
    def inner(x, y):
        print('calling ', func.__name__, 'with', x, 'and', y)
        func(x, y)
        print('returned from ', func.__name__)
    return inner

@logger
def my_func(x, y):
    print(x, y)

my_func(4, 5)
