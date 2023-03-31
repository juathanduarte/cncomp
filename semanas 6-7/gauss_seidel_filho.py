def gausJacobi(n, A, b, toler, iterMax):
    x = [0]*n
    v = [0]*n
    for i in range(n):
        x[i] = b[i]/A[i][i]
    iter = 0
    true = True
    while true:
        iter = iter + 1
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma = soma + A[i][j]*x[j]
            v[i] = (b[i] - soma)/A[i][i]
        normaNum = 0
        normaDen = 0
        for i in range(n):
            t = abs(v[i] - x[i])
            if t > normaNum:
                normaNum = t
            if abs(v[i]) > normaDen:
                normaDen = abs(v[i])
            x[i] = v[i]
        normaRel = normaNum/normaDen
        print(iter)
        print(x)
        print(normaRel)
        if (normaRel <= toler) or (iter >= iterMax):
            true = False
    if normaRel <= toler:
        info = 0
    else:
        info = 1

    return x, iter, info