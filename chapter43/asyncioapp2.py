import asyncio


async def worker():
    print('worker - will take some time')
    await asyncio.sleep(1)
    print('worker - Done it')
    return 42


def print_it(task):
    print('print_it result:', task.result())


async def do_something():
    print('do_something - create task for worker')
    task = asyncio.create_task(worker())

    print('do_something - add a callback')
    task.add_done_callback(print_it)

    await task

    # Information on task
    print('do_something - task.cancelled():', task.cancelled())
    print('do_something - task.done():', task.done())
    print('do_something - task.result():', task.result())
    print('do_something - task.exception():', task.exception())

    print('do_something - finished')


def main():
    print('Main - Starting')
    asyncio.run(do_something())
    print('Main - Done')


if __name__ == '__main__':
    main()
