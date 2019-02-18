# Using shared data between processes

from multiprocessing import Process, Value, Array


def worker(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


def main():
    print('Starting')

    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=worker, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(*arr)

    print('Done')


if __name__ == '__main__':
    main()
