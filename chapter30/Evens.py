class Evens(object):

    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    # Makes this class iterable
    def __iter__(self):
        return self

    # Makes this class an iterator
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val


print('Start')
for i in Evens(6):
    print(i, end=', ')

print('Done')




