import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Definir a função secante que recebe como parâmetros a função f, x0, x1 e a precisão.

x = Symbol('x')
f = (x**3) - (9*x) + 3
x0 = 0
x1 = 1
precision = 5 * 10**(-4)
df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

arrayX = []
arrayY = []

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
    
#Chamada do método da secante e printar a função com a raiz encontrada.
root = secante(f, x0, x1, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada.
x = np.linspace(-10, 10, 100)
y = f(x)
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Secante [-10, 10]')

x = np.linspace(-3, 3, 100)
y = f(x)
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