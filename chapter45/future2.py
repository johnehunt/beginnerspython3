from time import sleep
from concurrent.futures import ProcessPoolExecutor


def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    return i


print('Setting up the ThreadPoolExecutor')
pool = ProcessPoolExecutor(1)

print('Submitting the worker to the pool')
future = pool.submit(worker, 'A')

print('Obtained a reference to the future object', future)
print('future.result():', future.result())
print('Done')
