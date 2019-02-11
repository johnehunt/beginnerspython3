from multiprocessing import Process, Queue
from time import sleep


def worker(q):
    print('Worker - going to sleep')
    sleep(2)
    print('Worker - woken up and putting data on queue')
    q.put('Hello World')


def main():
    print('Main - Starting')
    q = Queue()
    p = Process(target=worker, args=(q,))
    print('Main - Starting the process')
    p.start()
    print('Main - waiting for data')
    print(q.get())
    print('Main - Done')


if __name__ == '__main__':
    main()
