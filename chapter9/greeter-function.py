def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)


greeter('John')
greeter('John', 'Hope you like Python')


def greeter(name, title='Dr', prompt='Welcome', message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)


greeter(message='We like Python', name='John')
greeter('John', message='We like Python')


def greeter(*names):
    for name in names:
        print('Welcome', name)


greeter('John', 'Denise', 'Phoebe', 'Adam')


def increment(num):
    return num + 1


print(increment(5))
print(increment(5))
