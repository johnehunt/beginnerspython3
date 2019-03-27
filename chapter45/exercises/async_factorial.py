import asyncio


async def factorial(num):
    if num == 0:
        return 1
    else:
        factorial_value = 1
        for i in range(1, num + 1):
            await asyncio.sleep(0.1)
            factorial_value = factorial_value * i
        return factorial_value


async def calculate_factorials(data):
    for async_func in asyncio.as_completed([factorial(v) for v in data]):
        result = await async_func
        print('calculate_factorials - result:', result)


def main():
    print('Main - Starting')
    asyncio.run(calculate_factorials([5, 7, 3, 6]))
    print('Main - Done')


if __name__ == '__main__':
    main()
