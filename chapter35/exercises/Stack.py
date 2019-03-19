class Stack:

    def __init__(self):
        self._list = []  # initial internal data

    def push(self, element):
        self._list.append(element)

    def pop(self):
        return self._list.pop()

    def top(self):
        return self._list[self.__len__() - 1]

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return self.__len__ == 0

    def __str__(self):
        return 'Stack: ' + str(self._list)


stack = Stack()
stack.push('T1')
stack.push('T2')
stack.push('T3')
print('stack:', stack)
print('stack.is_empty():', stack.is_empty())
print('len(stack):', len(stack))
print('stack.top():', stack.top())
print('stack.pop():', stack.pop())
print('stack:', stack)
