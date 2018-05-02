"""
A simple example using the Process class rather than pool. Might be better to
run this in the terminal. Using the process class makes it possible to do
pipelining and processing data as it comes in.
"""
import numpy as np
import os
import time
from multiprocessing import Process

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()


def process(files):
    print("Entering process")
    results = []
    for f in files:
        x = np.load(f)
        y = np.matmul(x, x)
        results.append(y)
    print("Exiting process")


if __name__ == '__main__':
    start_total = time.time()
    proc = Process(target=process, args=(files,))
    proc.start()
    proc.join()
    delta_total = time.time() - start_total
    print('Entire program took {:.3}s'.format(delta_total))
