#A equação de Kepler, usada para determinar órbitas de satélites é dada por: M = x – E sen(x) . Dado que E = 0.2 e M = 0.5, obtenha a raiz da equação de Kepler usando o método da Bissecção. Considere a = 0.0, b = 2.0 e precisão = 10^-3

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# x = Symbol('x')

m = lambda x: x - 0.2 * np.sin(x) - 0.5
a = 0.0
b = 2.0
precision = 10**(-3)

arrayX = []
arrayY = []

def bisect(m, a, b, precision):
    if m(a) * m(b) >= 0:
        print("Bisseção falhou")
        return None
    
    k = (a + b) / 2
    
    while abs(m(k)) >= precision:
        k = (a + b) / 2
        if m(k) == 0:
            return k
        if m(a) * m(k) < 0:
            b = k
        else:
            a = k
            
        arrayX.append(k)
        arrayY.append(m(k))
    return k

root = bisect(m, a, b, precision)
print(f"Raiz encontrada: {root}")

x = np.linspace(a, b, 100)
y = [m(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('m(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [a (0.0), b (2.0)]')
plt.grid()            

x = np.linspace(-3, 3, 100)
y = [m(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('m(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [-3, +3]')
plt.grid()

plt.subplots_adjust(hspace=0.7)
plt.show()