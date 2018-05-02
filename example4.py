"""
Same as example 3, but now we show that we can do other things in the meantime.
"""
import numpy as np
import os
from multiprocessing import Pool
import time

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()
results = []


def process(f):
    x = np.load(f)
    y = np.matmul(x, x)
    return f, np.mean(y)


def collect_result(result):
    results.append(result)


if __name__ == '__main__':
    start_total = time.time()

    p = Pool(2)
    for f in files:
        p.apply_async(process, kwds={'f': f}, callback=collect_result)
    p.close()

    time.sleep(1)
    print("""That is working off in the background, in the meantime we can do
whatever we please""")
    time.sleep(1)
    print("La la la la")
    time.sleep(1)
    print("La")
    time.sleep(1)
    print("Ok give me results now. Blocking until pool finished...")
    p.join()

    for f, r in results:
        print('The result of {} is {:.3}'.format(f, r))

    delta_total = time.time() - start_total
    print('Entire program took {:.3}s'.format(delta_total))

