import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

c_V1 = lambda x: 10 - 15 * (np.exp(-0.1 * x) - np.exp(-0.5 * x))
a_V1 = -1.0
b_V1 = 1.0
precision_V1 = 10**(-3)

x = Symbol('x')
f = 10 - 15 * (math.e ** (-0.1 * x) - math.e ** (-0.5 * x)) - 4
x0 = -1
x1 = 1
precision = 10**(-3)
df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

arrayX = []
arrayY = []

def bisect(f, a, b, precision):
    if f(a) * f(b) >= 0:
        print("Bisseção falhou")
        return None
    
    counter = 0
    m = (a + b) / 2
    
    while abs(f(m)) >= precision:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
            
        counter += 1
            
        arrayX.append(m)
        arrayY.append(f(m))
    
    print("Iterações: " + str(counter))
    return m

# print(f"\n" + 30 * "-" + "\n" + "Bisseção: " + str(bisect(c_V1, a_V1, b_V1, precision_V1)) + "\n" + 30 * "-")

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

# print(f"\n" + 30 * "-" + "\n" + "Posição Falsa: " + str(falsePosition(c_V1, a_V1, b_V1, precision_V1)) + "\n" + 30 * "-")

def newtonRaphson(f, x0, precision):    
    if(abs(f(x0)) < precision):
        print("Newton Raphson falhou")
        return None
    
    counter = 0
    k = x0 - f(x0)/f1(x0)
    
    while abs(f(x0)) >= precision:
        x0 = k
        k = x0 - f(x0)/f1(x0)
        
        counter += 1
        
        arrayX.append(k)
        arrayY.append(f(k))
        
    print("\nNewton Raphson | Iterações: " + str(counter))
    return x0

print(f"" + 30 * "-" + "\n" + "Newton Raphson | Raiz aproximada: " + str(newtonRaphson(f, 0.5, 10**(-4))) + "\n")

def secante(f, x0, x1, precision):
    if(abs(f(x0)) < precision) or (abs(f(x1)) < precision):
        print("Secante falhou")
        return None
    
    counter = 0
    
    while abs(f(x1)) >= precision or abs(f(x0)) >= precision:
        x2 = x1 - (f(x1) / (f(x1) - f(x0)) * (x1 - x0))

        # if abs(f(x2)) < precision or abs(x2 - x1) < precision:
        #     print
            
        #     # return x2
        
        x0 = x1
        x1 = x2      
        counter += 1
        
        arrayX.append(x2)
        arrayY.append(f(x2)) 
    
    print("Secante | Iterações: " + str(counter))
    return x1

print(f"" + 30 * "-" + "\n" + "Secante | Raiz aproximada: " + str(secante(f, x0, x1, precision)) + "\n" + 30 * "-")