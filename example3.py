"""
Another way of thinking about the speed up - here we use pool.apply_async. In
contrast to pool_map, the results don't come in in order, however we may see a
slight speed up as the processes don't have to block each other (if one
finishes before the other)
"""
import numpy as np
import os
from multiprocessing import Pool
import time

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()
results = []
# Define the number of processes to spin up
N = 2


def process(f):
    x = np.load(f)
    y = np.matmul(x, x)
    return f, np.mean(y)


def collect_result(result):
    results.append(result)


if __name__ == '__main__':
    start_total = time.time()

    p = Pool(N)
    for f in files:
        p.apply_async(process, kwds={'f': f}, callback=collect_result)
    p.close()
    p.join()

    for f, r in results:
        print('The result of {} is {:.3}'.format(f, r))

    delta_total = time.time() - start_total
    print('Entire program took {:.3}s'.format(delta_total))
