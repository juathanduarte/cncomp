#Em engenharia ambiental, a equação que se segue pode ser usada para calcular o nível de oxigênio, c, existente num rio a jusante de um local de descarga de esgoto, c = 10 − 15(e−0.1x − e−0.5x), em que x representa a distância a partir do local de descarga. Usando um método à sua escolha, determine o local (a partir da descarga) em que o nível de oxigênio atinge o valor 4. Considere [-1.0,1.0] e precisão = 10-3

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = Symbol('x')
c = 10 - 15 * (exp(-0.1 * x) - exp(-0.5 * x))
df = diff(c, x)
f1 = lambdify(x, c)
f = lambdify(x, df)

a = -1.0
b = 1.0
precision = 10**(-3)

arrayX = []
arrayY = []

def bisect(f, a, b, precision):
    if f(a) * f(b) >= 0:
        print("Bisseção falhou")
        return None
    
    m = (a + b) / 2
    
    while abs(f(m)) >= precision:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
            
        arrayX.append(m)
        arrayY.append(f(m))
    return m

def falsePosition(f, a, b, precision):
    if (f(a) * f(b) > 0):
        print("Posição falsa falhou")
        return None
    
    while abs(b - a) > precision:
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if (f(a) * f(x) < 0):
            b = x
        else:
            a = x
    
    return x

def secante(f, x0, x1, precision):
    if(abs(f(x0)) < precision) or (abs(f(x1)) < precision):
        print("Secante falhou")
        return None
    
    while abs(f(x1)) >= precision:
        x2 = x1 - (f(x1) / (f(x1) - f(x0)) * (x1 - x0))
        
        if abs(f(x2)) < precision:
            return x2
        
        x0 = x1
        x1 = x2
        
        arrayX.append(x2)
        arrayY.append(f(x2))
        
        return x2
    
    return None

def newtonRaphson(f, df, x0, precision):
    x1 = x0 - (f(x0) / df(x0))
    while abs(x1 - x0) > precision:
        x0 = x1
        x1 = x0 - (f(x0) / df(x0))
        
        arrayX.append(x1)
        arrayY.append(f(x1))
        
        return x1
    
    return x1

root = bisect(c, a, b, precision)
print(f"Raiz encontrada pela bisseção: {root}")