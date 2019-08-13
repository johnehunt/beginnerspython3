from abc import ABC, ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
# class Shape(ABC):

    def __init__(self, id):
        self._id = id

    @abstractmethod
    def display(self): pass

    @property
    @abstractmethod
    def id(self): pass


class Circle(Shape):

    def __init__(self, id):
        super().__init__(id)

    def display(self):
        print('Circle: ', self._id)

    @property
    def id(self):
        """ the id property """
        return self._id


def main():
    c = Circle("circle1")
    print(c.id)
    c.display()

if __name__ == '__main__':
    main()
