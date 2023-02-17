import math

f = lambda x: x**3 - 9*x + 5

def falsaPosicao(f, a, b, precision1, precision2):
    if f(a) * f(b) >= 0:
        print("Falsa posição falhou")
        return None
    
    while abs(b - a) >= precision1:
        m = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print("a: ", a, "b: ", b, "m: ", m, "f(m): ", f(m), "f(a): ", f(a))
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m

print("Resultado final: ", falsaPosicao(f, 0, 1, 0.0005, 0.01))