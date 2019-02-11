"""This is a test module"""

print('Hello I am the utils module')


def printer(some_object):
    print('printer')
    print(some_object)
    print('done')


class Shape:

    def __init__(self, id):
        self._id = id

    def __str__(self):
        return 'Shape - ' + self._id

    @property
    def id(self):
        """ The docstring for the id property """
        print('In id method')
        return self._id

    @id.setter
    def id(self, value):
        print('In set_age method')
        self._id = id


default_shape = Shape('square')


def _special_function():
    print('Special function')
