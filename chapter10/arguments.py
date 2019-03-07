def my_function(*args, **kwargs):
    for arg in args:
        print('arg:', arg)
    for key in kwargs.keys():
        print('key:', key, 'has value: ', kwargs[key])


my_function('John', 'Denise', daughter='Phoebe', son='Adam')
print('-' * 50)
my_function('Paul', 'Fiona', son_number_one='Andrew', son_number_two='James', daughter='Joselyn')


def named(**kwargs):
    for key in kwargs.keys():
        print('arg:', key, 'has value:', kwargs[key])


named(a=1, b=2, c=3)


def printer(*args):
    for arg in args:
        print('arg:', arg, end=", ")
    print()


a = (1, 2, 3, 4)
b = [1, 2, 3, 4]

printer(0, 1, 2, 3, 4, 5)
printer(0, a, 5)
printer(0, b, 5)
printer(0, *a)
printer(0, *b)
printer(0, *[1, 2, 3, 4])
