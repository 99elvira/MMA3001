import numpy as np

# function to generate Hilbert Matrix
def hilbert(n, dtype=float):
    i = np.arange(1, n+1, dtype=dtype)
    j = np.arange(1, n+1, dtype=dtype)
    return 1.0 / (i[:, None] + j[None, :] - 1.0)

# True variables
x_true = np.ones(5)

# Double precision system
A64 = hilbert(5, dtype=np.float64)

# generate solution
b64 = A64 @ x_true

# save to A matrix to file
np.save('A2.npy', A64)

# save to B matrix to file
np.save('b2.npy', b64)
