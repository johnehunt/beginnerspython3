from threading import Condition

class Stack:

    def __init__(self):
        self._list = []  # initial internal data
        # Set up condition to use to synchronise interactions
        self.condition = Condition()

    def push(self, element):
        with self.condition:
            self._list.append(element)
            self.condition.notify()

    def pop(self):
        with self.condition:
            self.condition.wait()
            return self._list.pop()

    def top(self):
        return self._list[self.length() - 1]

    def length(self):
        return len(self._list)

    def is_empty(self):
        return self.length() == 0

    def __str__(self):
        return 'Stack: ' + str(self._list)

