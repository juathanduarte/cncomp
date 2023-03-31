from numpy import dot

def eliminacao_gauss(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k]/A[k,k]
                A[i,k+1:n] = A[i,k+1:n] - lam*A[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(A[k,k+1:n],b[k+1:n]))/A[k,k]
    return b