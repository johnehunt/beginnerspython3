from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from time import sleep


def worker(msg):
    for i in range(0,10):
        print(msg,end='', flush=True)
        sleep(1)
    return i


print('Starting...setting up pool')
pool = ProcessPoolExecutor(3)
futures = []

print('Submitting futures')
future1 = pool.submit(worker, 'A')
futures.append(future1)
future2 = pool.submit(worker, 'B')
futures.append(future2)
future3 = pool.submit(worker, 'C')
futures.append(future3)
future4 = pool.submit(worker, 'D')
futures.append(future4)

print('Waiting for futures to complete')
wait(futures)

print('\nAll Done')
