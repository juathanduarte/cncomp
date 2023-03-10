import numpy as np

def jacobi(A, b, x0, tol, N):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x0
    for i in range(N):
        x = np.dot(np.linalg.inv(D), b - np.dot(LU, x))
        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x, i
    return x, N