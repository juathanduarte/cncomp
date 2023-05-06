import math
from math import sqrt
import numpy as np
from numpy import linalg
import sys
import pprint
import matplotlib.pyplot as plt
from scipy import integrate
from tabulate import tabulate

def trapezioChapraUmSegmento(h, f0, f1):
    trap1 = h * (f0 + f1) / 2
    
    return trap1

def trapComp(h, f, indiceInicial, indiceFinal):
    soma = f(indiceInicial)
    
    for i in range (indiceInicial, indiceFinal-1, 1):
        soma += 2 * f(i)
        
    soma += f(indiceFinal)
    
    return h * soma / 2

def simpson13(h, f0, f1, f2):
    simp13 = 2 * h * (f0 + 4 * f1 + f2) / 6
    
    return simp13

def simpson13MultiplosSegmentos (h, n, f):
    sum = f(0)
    
    for i in range(1, n - 2, 2):
        sum += 4 * f(i) + 2 * f(i + 1)
        
    sum += 4 * f(n - 1) + f(n)
    simp13m = h * sum / 3
    
    return simp13m

def simpson38(h, f0, f1, f2, f3):
    simp38 = 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8
    
    return simp38

def simp38(h, f, indiceInicial, indiceFinal):
    sum = 0
    
    for i in range(indiceInicial, indiceFinal - 2, 3):
        sum += simpson38(h, f(i), f(i + 1), f(i + 2), f(i + 3))
        
    return sum

def simpsonInt (a, b, n, f):
    h = (b - a) / n
    
    if n == 1:
        sum = trapezioChapraUmSegmento(h, f[n - 1], f[n])
    else:
        m = n
        odd = n / 2 - int(n / 2)
        
        if odd > 0 and n > 1:
            sum += simpson38(h, f[n - 3], f[n - 2], f[n - 1], f[n])
            
            m = n - 3
        
        if m > 1:
            sum += simpson13MultiplosSegmentos(h, m, f)
            
    simpInt = sum
    
    return simpInt
        
def euler(x0,y0,xn,n,h):
    x0Vector = []
    ynVector = []
    
    # h = tamanho do passo
    print('-----------Euler------------')
    print('-----------Solução------------')
    print('------------------------------')    
    print('x0\ty0\tf(x,y)\tyn')
    print('------------------------------')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        print('------------------------------')
        y0 = yn
        x0 = x0+h
        x0Vector.append(x0)
        ynVector.append(yn)
    
    print('\nX = %.4f,Y = %.4f' %(xn,yn))
    return x0Vector, ynVector

def rk4(x0,y0,xn,n, h):
    x0Vector = []
    ynVector = []
    
    print('---------Runge-Kutta---------')
    print('-----------Solução-----------')
    print('-----------------------------')    

    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn))
        print('-------------------------')
        
        y0 = yn
        x0 = x0+h
        x0Vector.append(x0)
        ynVector.append(yn)
        
    print('\nx=%.4f, y=%.4f' %(xn,yn))
    return x0Vector, ynVector
    
def erroAbsoluto(vexato,vaprox):
    erro = np.zeros(len(vexato))
    
    for i in np.arange(0,len(vexato)):
        erro[i] = abs(vexato[i] - vaprox[i])

    return erro    

def erroRelativoPercentual(vexato,vaprox):
    erro = np.zeros(len(vexato))
    
    for i in np.arange(0,len(vexato)):
        if vaprox[i] != 0:
            erro[i] = abs(vexato[i] - vaprox[i])/abs(vaprox[i]) * 100
        else:
            erro[i] = abs(vexato[i] - vaprox[i])
        
    return erro