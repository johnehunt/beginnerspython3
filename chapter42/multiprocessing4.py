from multiprocessing import Pool


def worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=4) as pool:
        for result in pool.imap_unordered(worker,
                                          [0, 1, 2, 3, 4, 5]):
            print(result)


if __name__ == '__main__':
    main()
