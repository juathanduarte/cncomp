import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Definir a função newtonRaphson que recebe como parâmetros a função f, o x0 e a precisão.

x = Symbol('x')
f = (x**3) - (9*x) + 3
x0 = 0.75
precision = 0.01
# f = (x**5) - (10/9) * (x**3) + (5/21) * x

df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

def newtonRaphson(f, x0, precision):    
    if(abs(f(x0)) < precision):
        print("Newton Raphson falhou")
        return None
    
    k = x0 - f(x0)/f1(x0)
    
    while abs(f(x0)) >= precision:
        x0 = k
        k = x0 - f(x0)/f1(x0)
    return x0

#Chamada do método de Newton Raphson e printar a função com a raiz encontrada.
root = newtonRaphson(f, x0, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada
x = np.linspace(-10, 10, 100)
y = f(x)
plt.plot(x, y, linestyle='-')
plt.plot(root, f(root), 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método de Newton Raphson')
plt.grid()
plt.show()