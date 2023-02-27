#Em problemas de fluxo em tubulações, é frequente precisar resolver a equação:c5 D5 + c1 D + c0 = 0. Se c5 = 1000, c1 = −3 e c0 = 9.04, determine a raiz usando o método de Newton-Raphson. Considere x0 = -0.5 e e = 10-3

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

d = Symbol('x')
f = 1000 * d**5 + (-3) * d + 9.04
x0 = -0.5
precision = 10**(-3)

df = f.diff(d)
f1 = lambdify(d, df)
f = lambdify(d, f)

arrayX = []
arrayY = []

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

print(f"\n" + 30 * "-" + "\n" + "Falsa Posição: " + str(newtonRaphson(f, x0, precision)) + "\n" + 30 * "-")

plt.figure(figsize=(10,10))
x = np.linspace(-0.5,0.5, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson [-10, 10]')
plt.grid()

x = np.linspace(-3, +3, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson [-3, 3]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()
