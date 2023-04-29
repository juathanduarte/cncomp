def newton(m, x, y, z):
    pz = 0
    dely = [0]*m
    for i in range(m):
        dely[i] = y[i]
        
    for i in range(1, m, 1):
        for k in range(m - 1, i + 1, -1):
            dely[k] = (dely[k] - dely[k - 1])/(x[k] - x[k - i])
            
    pz = dely[m - 1]
    
    for i in range(m - 1, 1, -1):
        pz = pz * (z - x[i]) + dely[i]
    
    return pz