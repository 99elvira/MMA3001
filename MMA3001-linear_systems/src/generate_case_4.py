import numpy as np

A = np.array([
    [2, -1, 3, 0.5, -1],
    [-1, 4, 1, 2, 3],
    [3, 1, -2, 1, 0.25],
    [1, 2, 1, -4, 2]
], dtype=float)

# True variables
x_true = np.ones(5)

b = A @ x_true

np.save('A4.npy',A)
np.save('b4.npy',b)
