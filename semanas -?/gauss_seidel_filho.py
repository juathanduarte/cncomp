def gauss_seidel(A, b, x, N=25, w=1.0):
    D = diag(A)
    R = A - diagflat(D)
    for i in range(N):
        x = (b - dot(R,x))/D
    return x