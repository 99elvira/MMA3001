import numpy as np

def A_5x5():
    A = np.array([
        [4, 1, 0, 0, 0],
        [1, 4, 1, 0, 0],
        [0, 1, 4, 1, 0],
        [0, 0, 1, 4, 1],
        [0, 0, 0, 1, 4],
    ], dtype=float)
    return A

def b_5x5():
    return np.array([1, 2, 3, 4, 5], dtype=float)

A = A_5x5()
b = b_5x5()

np.save('A1.npy',A)
np.save('b1.npy',b)
