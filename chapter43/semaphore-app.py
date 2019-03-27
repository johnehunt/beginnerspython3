from threading import Thread, Semaphore, currentThread
from time import sleep


def worker(semaphore):
    with semaphore:
        print(currentThread().getName() + " - entered")
        sleep(0.5)
        print(currentThread().getName() + " - exiting")


print('MainThread - Starting')

semaphore = Semaphore(2)
for i in range(0, 5):
    thread = Thread(name='T' + str(i), target=worker, args=[semaphore])
    thread.start()

print('MainThread - Done')
