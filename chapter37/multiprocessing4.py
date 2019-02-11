from multiprocessing import Pool


def worker(x):
    print('In worker with: ', x)
    print( x * x)

def main():
    with Pool(processes=4) as pool:
        print(pool.imap_unordered(worker,
                                  range(6)))


if __name__ == '__main__':
    main()
