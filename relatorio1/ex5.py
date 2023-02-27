#Determine a raiz f(x) = 2x⁴ + 4x³ + 3x² - 10x -15

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

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

fx = lambda x: sin(x) * x + 4
a = 1.0
b = 5.0
precision = 10**(-10)

print(f"\n" + 30 * "-" + "\n" + "Bissecção: " + str(bisect(fx, a, b, precision)) + "\n" + 30 * "-")

x = np.linspace(a, b, 100)
y = [fx(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [a, b]')
plt.grid()

x = np.linspace(2.9, 4.6, 100)
y = [fx(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [2.9, 4.6]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()

def falsePosition(f, a, b, precision):
    if (f(a) * f(b) >= 0):
        print("Falsa posição falhou")
        return None
    
    m = (a * f(b) - b * f(a)) / (f(b) - f(a))

    while abs(f(m)) >= precision:
        m = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
                    
        arrayX.append(m)
        arrayY.append(f(m))
    return m

fx = lambda x: sin(x) * x + 4
a = 1.0
b = 5.0
precision = 10**(-10)

print(f"\n" + 30 * "-" + "\n" + "Falsa Posição: " + str(falsePosition(fx, a, b, precision)) + "\n" + 30 * "-")

x = np.linspace(a, b, 100)
y = [fx(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Falsa Posição [a, b]')

x = np.linspace(-10, 10, 100)
y = [fx(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Falsa Posição [-10, 10]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()

def newtonRaphson(f, x0, precision):    
    if(abs(f(x0)) < precision):
        print("Newton Raphson falhou")
        return None
    
    k = x0 - f(x0)/f1(x0)
    
    while abs(f(x0)) >= precision:
        x0 = k
        k = x0 - f(x0)/f1(x0)
        arrayX.append(k)
        arrayY.append(f(k))
    
    return x0

x = Symbol('x')
f = sin(x) * x + 4
x0 = 1.0
precision = 10**(-10)
df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

print(f"\n" + 30 * "-" + "\n" + "Newton Raphson: " + str(newtonRaphson(f, x0, precision)) + "\n" + 30 * "-")

x = np.linspace(-10, 10, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson [-10, 10]')
plt.grid()

x = np.linspace(2.5, 5, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)') 
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson [2.5, 5]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()

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

x = Symbol('x')
f = (sin(x) * x) + 4
x0 = 1.0
x1 = 5.0
precision = 10**(-10)
f = lambdify(x, f)

print(f"\n" + 30 * "-" + "\n" + "Secante: " + str(secante(f, x0, x1, precision)) + "\n" + 30 * "-")

x = np.linspace(-10, 10, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Secante [-10, 10]')

x = np.linspace(4, 5, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Secante [-3, 3]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()