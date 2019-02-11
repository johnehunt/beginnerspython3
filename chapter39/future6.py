from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from random import randint


def is_even(n):
    print('Checking if', n , 'is even')
    sleep(randint(1, 5))
    return str(n) + ' ' + str(n % 2 == 0)


print('Started')
data = [1, 2, 3, 4, 5, 6]

pool = ThreadPoolExecutor(5)
futures = []

for v in data:
    futures.append(pool.submit(is_even, v))

for f in as_completed(futures):
    print(f.result())

print('Done')
