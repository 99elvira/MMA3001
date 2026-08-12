import numpy as np
from scipy.sparse import diags, kron, eye

def poisson_2d(n):
    """Return sparse SPD matrix for 2D Poisson equation."""
    e = np.ones(n)
    T = diags([e, -2*e, e], [-1, 0, 1], shape=(n, n))
    I = eye(n)
    A = kron(I, T) + kron(T, I)
    return A

def poisson_rhs_from_solution(n, u_func, laplace_u_func):
    """Generate b for Poisson matrix using analytic u and its Laplacian."""
    h = 1.0 / (n + 1)
    b = np.zeros(n*n)

    for i in range(n):
        for j in range(n):
            x = (i+1) * h
            y = (j+1) * h
            b[i*n + j] = -laplace_u_func(x, y)
    return b

# Example analytic solution
u = lambda x, y: np.sin(np.pi*x)*np.sin(np.pi*y)
lap_u = lambda x, y: 2*np.pi**2 * np.sin(np.pi*x)*np.sin(np.pi*y)

# stencil 5points
N = 30

b = poisson_rhs_from_solution(N, u, lap_u)

A = poisson_2d(N)  # 2500x2500 sparse SPD matrix

# note A is stored as a sparse matrix, not full matrix
# convert to dense matrix
Adense = A.toarray()

np.save('A5.npy',Adense)
np.save('b5.npy',b)
