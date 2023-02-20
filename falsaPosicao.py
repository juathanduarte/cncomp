import numpy as np
import matplotlib.pyplot as plt

#Definir a função falsePosition que recebe como parâmetros a função f, o intervalo [a, b] e a precisão.

f = lambda x: x**3 - 9*x + 5
a, b = 0, 1
precision = 0.0005

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
    return m

root = falsePosition(f, a, b, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada
x = np.linspace(a, b, 100)
y = f(x)
plt.plot(x, y)
plt.plot(root, f(root), 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Falsa Posição')
plt.show()