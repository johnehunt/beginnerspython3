from abc import ABC


class PrinterMixin(ABC):
    def print_me(self):
        print(self)


class IDPrinterMixin(ABC):
    def print_id(self):
        print(self.id)


class Person(object):
    def __init__(self, name):
        self.name = name


class Employee(Person, PrinterMixin, IDPrinterMixin):
    def __init__(self, name, age, id):
        super().__init__(name)
        self.age = age
        self.id = id

    def __str__(self):
        return 'Employee(' + self.id + ')' + self.name + '[' + str(self.age) + ']'


def main():
    e = Employee('Megan', 21, 'MS123')
    print(e)
    e.print_me()
    e.print_id()


if __name__ == '__main__':
    main()
