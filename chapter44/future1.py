from time import sleep
from concurrent.futures import ThreadPoolExecutor


# define function to be used with future
def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    return i


print('Setting up the ThreadPoolExecutor')
pool = ThreadPoolExecutor(1)

# Submit the function ot the pool to run
# concurrently - obtain a future from pool
print('Submitting the worker to the pool')
future1 = pool.submit(worker, 'A')

print('Obtained a reference to the future object', future1)

# Obtain the result form the future - wait if necessary
print('future1.result():', future1.result())

print('Done')
