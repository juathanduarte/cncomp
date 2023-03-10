def decomposicao_lu(A, b):
    n = len(A)
    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i][k]/A[k][k]
            A[i][k] = m
            for j in range(k+1, n):
                A[i][j] = A[i][j] - m*A[k][j]
    for i in range(n):
        for j in range(i+1, n):
            b[i] = b[i] - A[i][j]*b[j]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            b[i] = b[i] - A[i][j]*b[j]
        b[i] = b[i]/A[i][i]
    return b