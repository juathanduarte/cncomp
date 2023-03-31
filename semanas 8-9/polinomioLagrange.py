def polinomioLagrange(m, x, y, z):
    pz = 0
    for i in range(m):
        c = 1
        d = 1
        for j in range(m):
            if i != j:
                c = c*(z - x[j])
                d = d*(x[i] - x[j])
        pz = pz + c/d*y[i]
    return pz