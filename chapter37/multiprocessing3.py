# Using a Pool
from multiprocessing import Pool


def worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=4) as pool:
        print(pool.map(worker, range(6)))


if __name__ == '__main__':
    main()
