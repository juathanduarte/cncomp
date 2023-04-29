import numpy as np

def spline(abscissas, ordenadas):
    n=len(ordenadas)
    a = np.copy(ordenadas)
    b = [0] * (n-1)
    d = [0] * (n-1)
    h = [0] * (n-1)
    
    for i in range(n-1):
        h[i] = abscissas[i+1] - abscissas[i]

    A = [[1] + [0] * (n - 1)]
    
    for i in range(1, n-1):
        linha = [0] * n
        linha[i - 1] = h[i - 1]
        linha[i] = 2*(h[i-1] + h[i])
        linha[i+1] = h[i]
        A.append(linha)
        
    A.append([0] * (n-1) + [1])

    B = [0]
    
    for i in range(1, n-1):
        linha = 3*(a[i+1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i-1]
        B.append(linha)
    B.append(0)

    c =  np.linalg.solve(A, B)

    for i in range(n-1):
        b[i] = (a[i+1]-a[i])/h[i] - (h[i]/3)*(c[i+1]+2*c[i])
        d[i] = (c[i+1]-c[i])/(3*h[i])

    s = []

    for i in range(n-1):
        s.append(lambda x, j=i: d[j]*((x-abscissas[j])**3) + c[j]*((x-abscissas[j])**2) + b[j]*(x-abscissas[j]) + a[j])

    return s
