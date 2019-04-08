from concurrent.futures import ThreadPoolExecutor
from time import sleep


# Function to calculate factorials
def factorial(num):
    if num == 0:
        return 1
    else:
        factorial_value = 1
        for i in range(1, num + 1):
            sleep(0.1)
            factorial_value = factorial_value * i
        return factorial_value


# Function to print the result
def print_future_result(future):
    print('In callback Future result: ', future.result())


print('Started')
data = [5, 7, 3, 6]

pool = ThreadPoolExecutor(5)
for v in data:
    future = pool.submit(factorial, v)
    future.add_done_callback(print_future_result)

print('Done')
