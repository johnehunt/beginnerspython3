class ContextManagedClass(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    # Args exception type, exception value and traceback
    def __exit__(self, *args):
        print('__exit__:', args)
        return True

    def __str__(self):
        return 'ContextManagedClass object'


print('Starting')

with ContextManagedClass() as cmc:
    print('In with block', cmc)
    print('Exiting')

print('Done')
