from threading import Thread
from time import sleep

# Example extending the Thread class

class WorkerThread(Thread):
    def __init__(self, daemon=None, target=None, name=None):
        super().__init__(daemon=daemon, target=target, name=name)

    def run(self):
        for i in range(0, 10):
            print('.', end='', flush=True)
            sleep(1)


print('Starting')
t = WorkerThread()
t.start()
print('\nDone')
