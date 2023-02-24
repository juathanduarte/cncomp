import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Definir a função newtonRaphson que recebe como parâmetros a função f, o x0 e a precisão.

x = Symbol('x')
f = (x**3) - (9*x) + 3
x0 = 0.75
precision = 0.01
df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

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

#Chamada do método de Newton Raphson e printar a função com a raiz encontrada.
root = newtonRaphson(f, x0, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada
x = np.linspace(-10, 10, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson')
plt.grid()

x = np.linspace(-3, +3, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson')
plt.grid()
plt.show()

plt.show()