from collections.abc import MutableSequence


class Bag(MutableSequence):

    def __getitem__(self, index):
        pass

    def __delitem__(self, index):
        pass

    def __len__(self):
        pass

    def __setitem__(self, index, value):
        pass

    def insert(self, index, value):
        pass


def main():
    bag = Bag()
    print(bag)


if __name__ == '__main__':
    main()
