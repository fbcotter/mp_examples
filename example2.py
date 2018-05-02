"""
Easiest way to get a speed-up: calling the multiprocessing Pool.map function.
Instantly we can nearly halve the time it takes by using 2 processes to do this.
"""
import numpy as np
import os
from multiprocessing import Pool
import time

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()


def process(f):
    x = np.load(f)
    y = np.matmul(x, x)
    return np.mean(y)


if __name__ == '__main__':
    start_total = time.time()

    with Pool(2) as p:
        result = p.map(process, files)

    for r, f in zip(result, files):
        print('The result of {} is {:.3}'.format(f, r))

    delta_total = time.time() - start_total
    print('Entire program took {:.3}s'.format(delta_total))
