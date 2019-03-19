# Smaple Queue

queue = [] # Create an empty queue
queue.append('task1')
print('initial queue:', queue)
queue.append('task2')
queue.append('task3')
print('queue after additions:', queue)
element1 = queue.pop(0)
print('element retrieved from queue:', element1)
print('queue after removal', queue)


class Queue:

    def __init__(self):
        self._list = [] # initial internal data

    def enqueue(self, element):
        self._list.append(element)

    def dequeue(self):
        return self._list.pop(0)

    def __len__(self):
        """ Supports the len protocol """
        return len(self._list)

    def is_empty(self):
        return self.__len__() == 0

    def peek(self):
        return self._list[0]

    def __str__(self):
        return 'Queue: ' + str(self._list)


queue = Queue()
print('queue.is_empty():', queue.is_empty())
queue.enqueue('task1')
print('len(queue):', len(queue))
queue.enqueue('task2')
queue.enqueue('task3')
print('queue:', queue)
print('queue.peek():', queue.peek())
print('queue.dequeue():', queue.dequeue())
print('queue:', queue)
