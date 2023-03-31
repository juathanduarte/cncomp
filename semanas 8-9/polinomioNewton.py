def polinomioNewton(m, x, y, z):
    pz = 0
    for i in range(m):
        c = 1
        for j in range(i):
            c = c*(z - x[j])
        d = 1
        for j in range(i):
            d = d*(x[i] - x[j])
        pz = pz + c/d*y[i]
    return pz

# O que é o Dely?