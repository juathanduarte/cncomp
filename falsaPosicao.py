import numpy as np
import matplotlib.pyplot as plt

#Definir a função falsePosition que recebe como parâmetros a função f, o intervalo [a, b] e a precisão.

f = lambda x: x**3 - 9*x + 5
a, b = 0, 1
precision = 0.0005

arrayX = []
arrayY = []

def falsePosition(f, a, b, precision):
    if f(a) * f(b) >= 0:
        print("Falsa posição falhou")
        return None
    
    while abs(b - a) >= precision:
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

#Chamada do método da falsa posição e printar a função com a raiz encontrada.
root = falsePosition(f, a, b, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada
x = np.linspace(a, b, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Falsa Posição [a, b]')

x = np.linspace(-10, 10, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Falsa Posição [-10, 10]')

plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.show()