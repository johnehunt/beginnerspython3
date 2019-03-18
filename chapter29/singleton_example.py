def singleton(cls):
    print('In singleton for: ', cls)
    instance = None

    def get_instance():
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance

    return get_instance


@singleton
class Service(object):
    def print_it(self):
        print(self)


@singleton
class Foo(object):
    pass


print('Starting')
s1 = Service()
print(s1)
s2 = Service()
print(s2)
f1 = Foo()
print(f1)
f2 = Foo()
print(f2)
print('Done')
