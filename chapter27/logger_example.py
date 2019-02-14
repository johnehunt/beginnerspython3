def logger(func):
    def inner():
        print('calling ', func.__name__)
        func()
        print('called ', func.__name__)

    return inner


@logger
def target():
    print('In target function')


target()


def makebold(fn):
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"

    return makebold_wrapped


def makeitalic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"

    return makeitalic_wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


print(hello())


def register(active=True):
    def wrap(func):
        def wrapper():
            print('Calling ', func.__name__, ' decorator param ', active)
            if active:
                func()
                print('Called ', func.__name__)
            else:
                print('Skipped ', func.__name__)

        return wrapper

    return wrap


@register()
def func1():
    print('func1')


@register(active=False)
def func2():
    print('func2')


func1()
print('-' * 10)
func2()


def pretty_print(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper


class Person(object):

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_self(self):
        print('Person - ', self.name, ', ', self.age)

    @pretty_print
    def get_fullname(self):
        return self.name + " " + self.surname


print('Starting')
p = Person('John', 'Smith', 21)
p.print_self()
print(p.get_fullname())
print('Done')
