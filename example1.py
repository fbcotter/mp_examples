"""
Simple naive example of having to do lots of similar processing on large arrays
that takes time. Doing it sequentially is slow.
"""
import numpy as np
import os
import time

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()
means = []


def process(f):
    x = np.load(f)
    y = np.matmul(x, x)
    return np.mean(y)


if __name__ == '__main__':
    start_total = time.time()
    for f in files:
        start = time.time()
        m = process(f)
        means.append(m)
        delta_t = time.time() - start
        print('The result of {} is {:.3} - {:.3}s'.format(f, m, delta_t))
    delta_total = time.time() - start_total
    print('Entire program took {:.3}s'.format(delta_total))
