def trapezioChapraUmSegmento(h, f0, f1):
    trap1 = h * (f0 + f1) / 2
    
    return trap1

def trapezioChapraMultiplosSegmentos(h, n, f):
    sum = f[0]
    
    for i in n - 1:
        sum += 2 * f[i]
        
    sum = sum + f[n]
    trapm = h * sum / 2
    
    return trapm

def simpson13 (h, f0, f1, f2):
    simp13 = 2 * h * (f0 + 4 * f1 + f2) / 6
    
    return simp13

def simpson38 (h, f0, f1, f2, f3):
    simp38 = 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8
    
    return simp38

def simpson13MultiplosSegmentos (h, n, f):
    sum = f[0]
    
    for i in range(1, n - 2, 2):
        sum += 4 * f[i] + 2 * f[i + 1]
        
    sum += 4 * f[n - 1] + f[n]
    simp13m = h * sum / 3
    
    return simp13m

def simpsonInt (a, b, n, f):
    h = (b - a) / n
    
    if n == 1:
        sum = trapezioChapraUmSegmento(h, f[n - 1], f[n])
    else:
        m = n
        odd = n / 2 - int(n / 2)
        
        if odd > 0 and n > 1:
            sum += simpson38(h, f[n - 3], f[n - 2], f[n - 1], f[n])
            
            m = n - 3
        
        if m > 1:
            sum += simpson13MultiplosSegmentos(h, m, f)
            
    simpInt = sum
    
    return simpInt
        
def euler (a, b, y0, m, f):
    h = (b - a) / m
    x = a
    y = y0
    
    vetX = []
    vetY = []
    vetX[0] = x
    vetY[0] = y
    fxy = f(x[0], y[0])
    
    for i in range(m):
        x = a + i * h
        y = y + h * f(x, y)
        fxy = f(x[i], y[i])
        vetX[i + 1] = x
        vetY[i + 1] = y
    
    return vetX, vetY

