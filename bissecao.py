import math

f = lambda x: x**3 - 9*x + 5

def bissecao(f, a, b, precision):
    if f(a) * f(b) >= 0:
        print("Bisseção falhou")
        return None
    
    m = (a + b) / 2
    
    while abs(f(m)) >= precision:
        m = (a + b) / 2
        print("a: ", a, "b: ", b, "m: ", m, "f(m): ", f(m), "f(a): ", f(a))
        if f(m) == 0:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m
    
print("Resultado final: ", bissecao(f, 0.5, 1, 0.01))