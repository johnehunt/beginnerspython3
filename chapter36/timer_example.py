from threading import Timer


def hello():
    print("hello")


print('Starting')
t = Timer(5, hello)
t.start()
print('Done')
