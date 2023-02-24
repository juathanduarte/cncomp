import numpy as np
import matplotlib.pyplot as plt

#Definir a função bisect que recebe como parâmetros a função f, o intervalo [a, b] e a precisão
f = lambda x: x**3 - 9*x + 5
a, b = 0.5, 1
precision = 0.01

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
    
#Chamada do método da bissecção e printar a função com a raiz encontrada.
root = bisect(f, a, b, precision)
print(f"Raiz encontrada: {root}")

#Plotar as funções e raízes encontradas, mudando o intervalo de plotagem.
x = np.linspace(a, b, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [a, b]')
plt.grid()

x = np.linspace(-3, 3, 100)
y = [f(x) for x in x]
plt.subplot(2, 1, 2)
plt.plot(x, y, linestyle='-')
plt.plot(arrayX, arrayY, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(y=0, color='red')
plt.title('Método da Bissecção [-3, +3]')

plt.grid()
plt.subplots_adjust(hspace=0.7)
plt.show()