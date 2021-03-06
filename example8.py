"""
Shows how we can use the Process.is_alive function to check whether we should
exit or not.
"""
import numpy as np
import os
# Note we import the queue from multiprocessing, but the Empty exception comes
# from the older queue module
from multiprocessing import Process, Queue
from queue import Empty
import time

files = os.listdir('.')
files = [f for f in files if os.path.splitext(f)[1] == '.npy']
files.sort()
# Define the number of processes to spin up
N = 2


def process(f):
    x = np.load(f)
    y = np.matmul(x, x)
    return np.mean(y)


def process_files(files, result_q):
    for f in files:
        y = process(f)
        result_q.put((f, y))


def split_work(files, N):
    """ Splits a list into a list of N sublists, each with roughly equal size
    """
    # Get a a list of the indices which would denote N intervals
    b = np.linspace(0, len(files), N, endpoint=False, dtype='int')
    # Add the last index to this list
    b = np.append(b, [len(files)])
    # Convert this list to tuples of start and end indices
    b = [(b[i], b[i+1]) for i in range(len(b)-1)]
    # Use this to index the files list and return a list of lists
    return [files[l:u] for l,u in b]


if __name__ == '__main__':
    start_total = time.time()
    result_queue = Queue()

    procs = []
    proc_files = split_work(files, N)
    for i in range(N):
        proc = Process(target=process_files, args=(proc_files[i], result_queue))
        proc.start()
        procs.append(proc)

    while True:
        data = False
        try:
            f, r = result_queue.get(timeout=5)
            data = True
        except Empty:
            # Check if any of the feeders are still alive, if not, quit
            alive = [proc.is_alive() for proc in procs]
            if True not in alive:
                print("Timeout on queue retrieval and feeders dead")
                break

        # Need to check that the queue.get() method above worked - could have
        # had a timeout and a process was alive
        if data:
            print('The result of {} is {:.3}'.format(f, r))

    # Don't need to join really, we've already tested that they are all finished
    [proc.join() for proc in procs]
