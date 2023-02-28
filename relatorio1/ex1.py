import numpy as np
import matplotlib.pyplot as plt
from sympy import *

m = lambda x: x - 0.2 * np.sin(x) - 0.5
a = 0.0
b = 2.0
precision = 10**(-3)

arrayX = []
arrayY = []

def showGraphic(f, titulo, x1_start, x1_end, x2_start, x2_end, arrayX, arrayY):
    plt.figure(figsize=(10,10))
    plt.suptitle(titulo, fontsize="16")
    
    plt.subplot(2, 1, 1)
    curva = np.linspace(x1_start, x1_end, 100)
    valores = [f(x) for x in curva]
    plt.plot(curva, valores, linestyle='-')
    plt.plot(arrayX, arrayY, 'ro')
    plt.title(' X = [' + str(x1_start) + ', ' + str(x1_end) + ']')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(y=0, color='red')
    plt.grid()
    
    plt.subplot(2, 1, 2)
    curva = np.linspace(x2_start, x2_end, 100)
    valores = [f(x) for x in curva]
    plt.plot(curva, valores, linestyle='-')
    plt.plot(arrayX, arrayY, 'ro')
    plt.title(' X = [' + str(x2_start) + ', ' + str(x2_end) + ']')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(y=0, color='red')
    plt.grid()
    
    plt.show()

def bisect(m, a, b, precision):
    if m(a) * m(b) >= 0:
        print("Bisseção falhou")
        return None
    
    counter = 0
    k = (a + b) / 2
    
    while abs(m(k)) >= precision:
        k = (a + b) / 2
        if m(k) == 0:
            return k
        if m(a) * m(k) < 0:
            b = k
        else:
            a = k
        
        counter += 1
    
        arrayX.append(k)
        arrayY.append(m(k))

    print("Iterações: " + str(counter))
    return k

print(f"" + 30 * "-" + "\n" + "Raiz aproximada: " + str(bisect(m, a, b, precision)) + "\n" + 30 * "-")

showGraphic(m, "Método da Bissecção", a, b, -30, 30, arrayX, arrayY)

# plt.figure(figsize=(10,10))

# x = np.linspace(a, b, 100)
# y = [m(x) for x in x]
# plt.subplot(2, 1, 1)
# plt.plot(x, y, linestyle='-')
# plt.plot(arrayX, arrayY, 'ro')
# plt.xlabel('x')
# plt.ylabel('m(x)')
# plt.axhline(y=0, color='red')
# plt.title('Método da Bissecção [a (0.0), b (2.0)]')
# plt.grid()            

# x = np.linspace(-30, 30, 100)
# y = [m(x) for x in x]
# plt.subplot(2, 1, 2)
# plt.plot(x, y, linestyle='-')
# plt.plot(arrayX, arrayY, 'ro')
# plt.xlabel('x')
# plt.ylabel('m(x)')
# plt.axhline(y=0, color='red')
# plt.title('Método da Bissecção [-30, +30]')
# plt.grid()

# plt.subplots_adjust(hspace=0.2)
# plt.show()
    
    
    