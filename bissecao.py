import numpy as np
import matplotlib.pyplot as plt

#Definir a função bisect que recebe como parâmetros a função f, o intervalo [a, b] e a precisão
f = lambda x: x**3 - 9*x + 5
a, b = 0.5, 1
precision = 0.01

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
    return m
    
#Chamada do método da bissecção
root = bisect(f, a, b, precision)
print(f"Raiz encontrada: {root}")

#Plotar a função e a raiz encontrada
x = np.linspace(a, b, 100)
y = f(x)
plt.plot(x, y)
plt.plot(root, f(root), 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método da Bissecção')
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# # Definir a função f(x), o intervalo [a, b] e a precisão
# f = lambda x: x**3 - 9*x + 5
# a, b = 0.5, 1
# precision = 0.01

# def bisect(f, a, b, precision):
#     if (b - a) < precision:
#         print("Bissecção falhou")
#         return None
    
#     m = f(a)
#     x = (a + b) / 2
    
#     while abs(f(x)) >= precision:
#         fc = f(x)
#         if fc == 0:
#             return x
#         if m * fc < 0:
#             b = m
#         else:
#             a = m
#     return m

# #Chamada do método da bissecção
# root = bisect(f, a, b, precision)
# print(f"Raiz encontrada: {root}")

# # Plotar a função e a raiz encontrada
# x = np.linspace(a, b, 100)
# y = f(x)
# plt.plot(x, y)
# plt.plot(root, f(root), 'ro')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Método da Bissecção')
# plt.show()
