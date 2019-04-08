# Using a Pool
from multiprocessing import Pool


def worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=4) as pool:
        print(pool.map(worker, [0, 1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
