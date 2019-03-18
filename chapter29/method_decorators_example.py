def pretty_print(method):
    def method_wrapper(self):
        return "<p>{0}</p>".format(method(self))

    return method_wrapper


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


def trace(method):
    def method_wrapper(self, x, y):
        print('Calling', method, 'with', x, y)
        method(self, x, y)
        print('Called', method, 'with', x, y)
    return method_wrapper

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @trace
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point - ' + str(self.x) + ',' + str(self.y)


p = Point(1, 1)
print(p)
p.move_to(5, 5)
print(p)

