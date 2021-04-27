class Stack:

    def __init__(self):
        self._list = []  # initial internal data

    def push(self, element):
        self._list.append(element)

    def pop(self):
        return self._list.pop()

    def top(self):
        return self._list[self.length() - 1]

    def length(self):
        return len(self._list)

    def is_empty(self):
        return self.length() == 0

    # Makes the Stack iterable
    def __iter__(self):
        return iter(self._list)

    def __str__(self):
        return 'Stack: ' + str(self._list)


# Define functions to use with map and filter
def add_item(item):
    return 'item: ' + item


def is_job(item):
    if item.startswith('Job'):
        return True
    else:
        return False


stack = Stack()
stack.push('Task1')
stack.push('Task2')
stack.push('Job1')
stack.push('Task3')
stack.push('Job2')
print('stack contents:', stack)

# Apply functions to stack contents using map and filter
new_list = list(map(add_item, stack))
print('new_list:', new_list)

filtered_list = list(filter(is_job, stack))
print('filtered_list: ', filtered_list)
