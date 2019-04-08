from threading import Timer


def hello():
    print("hello")


print('Starting')

# Set up timer to wait 5 seconds
# and then run hello function
t = Timer(5, hello)
t.start()

print('Done')
