from threading import Thread


def simple_worker():
    print('hello')


# Create a new thread and start it
# The thread will run the function simple_worker
t1 = Thread(target=simple_worker)
t1.start()
