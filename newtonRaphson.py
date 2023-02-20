from sympy import *

x = Symbol('x')
# f = (x**5) - (10/9) * (x**3) + (5/21) * x
f = (x**3) - (9*x) + 3

df = f.diff(x)
f1 = lambdify(x, df)
f = lambdify(x, f)

iterations = []
iterations1 = []

def newtonRaphson(f, x0, precision):    
    if(abs(f(x0)) < precision):
        print("Newton Raphson falhou")
        return None
    
    k = x0 - f(x0)/f1(x0)
    
    while abs(f(x0)) >= precision:
        x0 = k
        k = x0 - f(x0)/f1(x0)
        
        iterations.append(x0)
        iterations1.append(f(x0))
        print(iterations)
        print(iterations1)
    return x0

print(newtonRaphson(f, 0.75, 0.01))