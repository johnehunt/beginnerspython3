from threading import Thread
from time import sleep


def worker():
    for i in range(0, 10):
        print('.', end='', flush=True)
        sleep(1)


print('Starting')

# Create read object with reference to worker function
t = Thread(target=worker)
# Start the thread object 
t.start()
# Wait for the thread to complete 
t.join()

print('\nDone')
