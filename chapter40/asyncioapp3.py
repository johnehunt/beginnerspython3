import asyncio
import random


async def worker():
    print('Worker - will take some time')
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print('Worker - Done it')
    return result


async def do_something():
    print('do_something - will wait for worker')
    # Run three calls to worker concurrently and collect results
    results = await asyncio.gather(worker(), worker(), worker())
    print('results from calls:', results)


def main():
    print('Main - Starting')
    asyncio.run(do_something())
    print('Main - Done')


if __name__ == '__main__':
    main()
