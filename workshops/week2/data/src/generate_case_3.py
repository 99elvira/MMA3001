import numpy as np

A64 = np.array([
    [3.271428391e8,  1.552948112e9,  9.114228551e7,  4.771992331e6,  8.221551992e5],
    [6.542856782e8,  3.104896224e9,  1.823845710e8,  9.543984662e6,  1.644310398e6],
    [9.814285173e8,  4.657844336e9,  2.735268565e8,  1.431597699e7,  2.466465597e6],
    [4.200551882331e12, 8.100992551441e12, 1.210448228551e13,
     1.610771992331e13, 2.010551992331e13],
], dtype=np.float64)

row4 = A64[3]

factor = 4.1758690198181   # non‑trivial, not visually obvious

row5 = row4 * factor

A64 = np.vstack([A64, row5])

# True variables
x_true = np.ones(5)

b64 = A64 @ x_true

# save to file
np.save('A3.npy',A64)
np.save('b3.npy',b64)
