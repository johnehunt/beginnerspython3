def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)


greeter('Eloise')
greeter('Eloise', 'Hope you like Rugby')


def greeter(name, title='Dr', prompt='Welcome', message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)


greeter(message='We like Python', name='Lloyd')
greeter('Lloyd', message='We like Python')


def greeter(*names):
    for name in names:
        print('Welcome', name)


greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')


def increment(num):
    return num + 1


print(increment(5))
print(increment(5))
