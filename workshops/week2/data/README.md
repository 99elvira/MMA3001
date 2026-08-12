# MMA3001-linear_systems
A series of sample linear systems.

Matrices for each system are stored as NumPy binary *.npy files 
using the NumPY save and load functions below.

```
import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Export to binary
np.save('my_matrix.npy', matrix)

# Reload it later
loaded_matrix = np.load('my_matrix.npy')
```

To load the A matrix and b vector for each case,
```
from load_systems import case

A1,b1 = case(1) # for example 1
A2,b2 = case(2) # for example 2
```


# Example Linear Systems $\mathbf{A}\cdot\mathbf{x}=\mathbf{b}$

## Example 1
Is a square matrix (5x5) matrix

$$\mathbf{A} = \begin{bmatrix} 4 & 1 & 0 & 0 & 0\\
1 & 4 & 1 & 0 & 0\\
0 & 1 & 4 & 1 & 0\\
0 & 0 & 1 & 4 & 1\\
0 & 0 & 0 & 1 & 4
\end{bmatrix}$$

and 

$$\mathbf{b} = \begin{bmatrix} 1\\ 
2 \\ 
3 \\ 
4 \\ 
5 \end{bmatrix}$$

## Example 2 - Hilbert Matrix
The Hilbert Matrix is a square matrix with entries being the unit fractions

$$H_{ij}=\frac{1}{i+j-1}$$

Consider a system where 

$$\mathbf{A} = H_{ij} = \begin{bmatrix} 1 & \frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \frac{1}{5}\\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \frac{1}{5} & \frac{1}{6}\\
\frac{1}{3} & \frac{1}{4} & \frac{1}{5} & \frac{1}{6} & \frac{1}{7}\\
\frac{1}{4} & \frac{1}{5} & \frac{1}{6} & \frac{1}{7} & \frac{1}{8}\\
\frac{1}{5} & \frac{1}{6} & \frac{1}{7} & \frac{1}{8} & \frac{1}{9}
\end{bmatrix}$$

and

$$b_i = \sum^5_{j=0}H_{ij}$$

or

$$\mathbf{b} = \begin{bmatrix} 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5}\\
\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\\
\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7}\\
\frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}\\
\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9}
\end{bmatrix}$$

## Example 3

$$\mathbf{A} = \begin{bmatrix} 3.271428391e8 & 1.552948112e9 & 9.114228551e7 & 4.771992331e6 & 8.221551992e5\\
6.542856782e8 & 3.104896224e9 & 1.823845710e8 & 9.543984662e6 & 1.644310398e6\\
9.814285173e8 & 4.657844336e9 & 2.735268565e8 & 1.431597699e7 & 2.466465597e6\\
4.200551882331e12 & 8.100992551441e12 & 1.210448228551e13 & 1.610771992331e13 & 2.010551992331e13\\
1.754507980393723e+13 & 3.385699598533067e+13 & 5.061124759430723e+13 & 6.727481676393723e+13 & 8.398622020393723e+13\\
\end{bmatrix}$$

and 

$$\mathbf{b} = \begin{bmatrix} 1\\ 
2 \\ 
3 \\ 
4 \\ 
5 \end{bmatrix}$$

## Example 4

$$\mathbf{A} = \begin{bmatrix} 2 & -1 & 3 & 0.5 & -1\\
-1 & 4 & 1 & 2 & 3\\
3 & 1 & -2 & 1 & 0.25\\
1 & 2 & 1 & -4 & 2
\end{bmatrix}$$

and 

$$\mathbf{b} = \begin{bmatrix} 3.5\\ 
9 \\ 
3.25 \\ 
2 \end{bmatrix}$$


## Example 5 
Same as Example 3 except all value are converted to single precision.

## Example 5 - Poisson 2D Laplacian (5‑Point Stencil)

We consider the 2D Poisson equation:

    -∇²u(x, y) = f(x, y)

On a uniform n×n grid with spacing h = 1/(n+1), the Laplacian is approximated using
the standard 5‑point finite‑difference stencil. For an interior grid point (i, j):

    -∇²u ≈ (1/h²) * (4*u[i,j]
                     - u[i-1,j]
                     - u[i+1,j]
                     - u[i,j-1]
                     - u[i,j+1])

This couples each grid point to its four nearest neighbours.

Stencil layout:

          (i, j+1)
              |
    (i-1, j) — (i, j) — (i+1, j)
              |
          (i, j-1)

The resulting linear system Au = b has size N = n². The matrix A is sparse,
symmetric, positive‑definite, and strictly diagonally dominant. Each row contains
at most five non‑zero entries: one main diagonal term (4/h²) and up to four
off‑diagonal neighbour terms (-1/h²).

The matrix has a block‑tridiagonal structure that can be written as:

    A = kron(I, T) + kron(T, I)

where T is the 1D second‑difference matrix:

    T = diag([-1, -1], offsets=[-1, 1]) + diag([2], offset=0)

For example, when n = 4 (so N = 16), the matrix pattern looks like:

    [ 4 -1  0 -1  ... ]
    [ -1 4 -1  0  ... ]
    [ 0 -1  4 -1  ... ]
    [ -1 0 -1  4  ... ]
    [ ...             ]

Right-hand side vector b for the 2D Poisson equation

We solve the discrete Poisson equation:

    A u = b

where A is the matrix produced by the 5‑point Laplacian stencil. The vector b
contains the discretised values of the source term f(x, y).

We assume the continuous PDE:

    -∇²u(x, y) = f(x, y)

To construct b, we evaluate f(x, y) at each interior grid point. For an n×n grid,
the spacing is:

    h = 1 / (n + 1)

Interior grid points have coordinates:

    x_i = (i + 1) * h
    y_j = (j + 1) * h

for i, j = 0, 1, ..., n-1.

The right-hand side entry corresponding to grid point (i, j) is:

    b[k] = f(x_i, y_j)

where k = i*n + j is the flattened index.

If the PDE is written as:

    -∇²u = f

then the discrete equation becomes:

    (1/h²) * (4*u[i,j]
              - u[i-1,j]
              - u[i+1,j]
              - u[i,j-1]
              - u[i,j+1]) = f(x_i, y_j)

Multiplying both sides by h² gives the linear system:

    A u = b

with:

    b[k] = h² * f(x_i, y_j)

This scaling ensures that the discrete operator matches the continuous PDE.

Summary:
- b stores the values of the source term f(x, y) at interior grid points.
- Each entry is scaled by h².
- The ordering of b matches the row ordering of A (row-major flattening).
- Boundary conditions modify b if Dirichlet or Neumann terms are present.

Example:
If f(x, y) = 1 everywhere, then:

    b[k] = h²

for all interior points.



