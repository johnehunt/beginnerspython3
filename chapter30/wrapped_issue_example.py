from functools import wraps


def logger(func):
    @wraps(func)
    def inner():
        print('calling ', func.__name__)
        func()
        print('called ', func.__name__)

    return inner


@logger
def get_text(name):
    """returns some text"""
    return "Hello " + name


print('name:', get_text.__name__)
print('doc: ', get_text.__doc__)
print('module; ', get_text.__module__)
