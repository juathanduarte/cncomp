def gaussiana(matrizA, b, n, pivot=True):
    det = 1
    info = 0
    for j in range(n):
        p = j
        aMax = abs(matrizA[j][j])
    
        if(pivot):
            aMax, p = pivotacao(j, matrizA, n, p)
        if p != j:
            for k in range(n):
                t = matrizA[j][k]
                matrizA[j][k] = matrizA[p][k]
                matrizA[p][k] = t
            t = b[j]
            b[j] = b[p]
            b[p] = t
            det  = (det * -1)
        det = det * matrizA[j][j]
        if abs(matrizA[j][j]) != 0:
            r = 1/matrizA[j][j]
            for i in range(j+1, n):
                mult = matrizA[i][j] * r
                matrizA[i][j] = 0
                for k in range(j+1, n):
                    matrizA[i][k] = matrizA[i][k] - (mult * matrizA[j][k])
                b[i] = b[i] - (mult * b[j])
        else:
            if info == 0:
                info = j
    det = det * matrizA[n-1][n-1]
    if(info == 0 and abs(matrizA[n-1][n-1])):
        info = n
    return matrizA, b, det, info
