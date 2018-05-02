import numpy as np

for i in range(10):
    a = np.random.randn(15, 500, 500)
    np.save('filter%d.npy' % i, a)
