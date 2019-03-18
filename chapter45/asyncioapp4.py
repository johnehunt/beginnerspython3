import asyncio
import random


async def worker(label):
    print('Worker - will take some time')
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print('Worker - Done it')
    return label + str(result)


async def do_something():
    print('do_something - will wait for worker')
    # Run three calls to worker concurrently and collect results
    for async_func in asyncio.as_completed((worker('A'), worker('B'), worker('C'))):
        result = await async_func
        print('do_something - result:', result)


def main():
    print('Main - Starting')
    asyncio.run(do_something())
    print('Main - Done')


if __name__ == '__main__':
    main()
