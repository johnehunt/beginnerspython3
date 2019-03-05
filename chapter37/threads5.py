from threading import Thread
from time import sleep


def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


d = Thread(daemon=True, target=worker, args=('C'))
d.start()
