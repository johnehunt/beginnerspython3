from multiprocessing import Pool


def collect_results(result):
    print('In collect_results: ', result)


def worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=2) as pool:
        # get based example
        res = pool.apply_async(worker, [6])
        print('Result from async: ', res.get(timeout=1))

    with Pool(processes=2) as pool:
        # callback based example
        pool.apply_async(worker, args=[4],
                         callback=collect_results)


if __name__ == '__main__':
    main()
