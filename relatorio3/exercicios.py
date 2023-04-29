import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import ln

def lagrange(m, x, y, z):
    pz = 0

    for i in range(m):
        c = 1
        d = 1

        for j in range(m):
            if i != j:
                c = c*(z - x[j])
                d = d*(x[i] - x[j])
        pz = pz + c/d*y[i]
        
    return pz

def newton(m, x, y, z):
    pz = 0
    dely = [0]*m
    
    for i in range(m):
        dely[i] = y[i]
        
    for i in range(1, m, 1):
        for k in range(m - 1, i + 1, -1):
            dely[k] = (dely[k] - dely[k - 1])/(x[k] - x[k - i])
            
    pz = dely[m - 1]
    
    for i in range(m - 1, 1, -1):
        pz = pz * (z - x[i]) + dely[i]
    
    return pz

def spline(abscissas, ordenadas):
    n=len(ordenadas)
    a = np.copy(ordenadas)
    b = [0] * (n-1)
    d = [0] * (n-1)
    h = [0] * (n-1)
    
    for i in range(n-1):
        h[i] = abscissas[i+1] - abscissas[i]

    A = [[1] + [0] * (n - 1)]
    
    for i in range(1, n-1):
        linha = [0] * n
        linha[i - 1] = h[i - 1]
        linha[i] = 2*(h[i-1] + h[i])
        linha[i+1] = h[i]
        A.append(linha)
        
    A.append([0] * (n-1) + [1])

    B = [0]
    
    for i in range(1, n-1):
        linha = 3*(a[i+1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i-1]
        B.append(linha)
    B.append(0)

    c =  np.linalg.solve(A, B)

    for i in range(n-1):
        b[i] = (a[i+1]-a[i])/h[i] - (h[i]/3)*(c[i+1]+2*c[i])
        d[i] = (c[i+1]-c[i])/(3*h[i])

    s = []

    for i in range(n-1):
        s.append(lambda x, j=i: d[j]*((x-abscissas[j])**3) + c[j]*((x-abscissas[j])**2) + b[j]*(x-abscissas[j]) + a[j])

    return s

def dispersalGraphic(param1, param2, param3, param2Title, param3Title, xLabelTitle, yLabelTitle):
    if (param3 != ' '):
        plt.scatter(param1, param2, label=param2Title, color='red')
        plt.scatter(param1, param3, label=param3Title, color='blue')
        plt.xlabel(xLabelTitle)
        plt.ylabel(yLabelTitle)
        plt.legend()
        plt.show()
    else:
        plt.scatter(param1, param2, label=param3Title, color='red')
        plt.xlabel(param2Title)
        plt.ylabel(param3Title)
        plt.xlabel(xLabelTitle)
        plt.ylabel(yLabelTitle)
        plt.legend()
        plt.show()

def lineGraphic(param1, param2, param3, a_param2, b_param2, a_param3, b_param3, xLabelTitle, yLabelTitle, titleParam2, titleParam3, regressionTitleParam2, regressionTitleParam3):
    if (param3 != ' '):
        plt.scatter(param1, param2, color='red', label=titleParam2)
        plt.scatter(param1, param3, color='blue', label=titleParam3)

        plt.plot(param1, [a_param2 * x + b_param2 for x in param1], color='red', label=regressionTitleParam2)

        interp_x = np.linspace(min(param1), max(param1), 300)
        interp_y = np.interp(interp_x, param1, param3)
        plt.plot(interp_x, interp_y, color='blue', label=regressionTitleParam3)

        plt.xlabel(xLabelTitle)
        plt.ylabel(yLabelTitle)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        plt.scatter(param1, param2, color='red')

        interp_x = np.linspace(min(param1), max(param1), 300)
        interp_y = np.interp(interp_x, param1, param2)
        plt.plot(interp_x, interp_y, color='red')

        plt.xlabel(xLabelTitle)
        plt.ylabel(yLabelTitle)
        plt.grid(True)
        plt.show()

def regressaoLinear(x, y):  
    n = len(x)
    x2 = [0]*n
    xy = [0]*n
    somaX = 0
    somaY = 0
    somaX2 = 0
    somaXY = 0
    a = 0
    b = 0

    for i in range(n):
        x2[i] = x[i] * x[i]
        xy[i] = x[i] * y[i]
        somaX = somaX + x[i]
        somaY = somaY + y[i]
        somaX2 = somaX2 + x2[i]
        somaXY = somaXY + xy[i]

    a = (n * somaXY - somaX * somaY) / (n * somaX2 - somaX * somaX)
    b = (somaY - a * somaX) / n

    return a, b

def mmqGrau1(x,y):
    n=len(x)
    sumx=0
    sumy=0
    sumxy=0
    sumx2=0
    st=0
    sr=0
    a1=0
    a0=0
    syx=0
    r2=0
    for i in np.arange(0,n):
        sumx = sumx + x[i]
        sumy = sumy + y[i]
        sumxy = sumxy + x[i]*y[i]
        sumx2 = sumx2 + x[i]*x[i]
    xm = sumx/n
    ym = sumy/n
    a1 = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx*sumx)
    a0 = ym - a1*xm
    for i in np.arange(0,n):
        st = st + (y[i]-ym)*(y[i]-ym)
        sr = sr + (y[i]- a1*x[i]-a0)*(y[i]- a1*x[i]-a0)
    syx = math.sqrt(sr/(n-2))
    r2 = (st-sr)/st
  
    return (a1,a0)

def mmqGrau2(x, y):
    h = np.zeros((3, len(x)))

    for i in range(len(h)):
        for j in range(len(h[0])):
            h[i][j] = pow(x[j], i)

    a = np.zeros((3, 3))
    b = np.zeros(3)
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j] = h[i].dot(h[j])
        b[i] = h[i].dot(y)
  
    c = np.linalg.solve(a, b)

    return (c[2],c[1],c[0])

# dia = [0, 4, 8, 12, 16, 20]
# quantidade = [67.38, 74.67, 82.74, 91.69, 101.60, 112.58]

# dispersalGraphic(dia, quantidade, ' ', 'Dia', 'Quantidade', ' ', ' ')

# a_quantidade, b_quantidade = regressaoLinear(dia, quantidade)
# print("\n---Quantidade---")
# print("Coeficientes de regressão linear para a componente de quantidade:")
# print("Interceptação (a):", a_quantidade)
# print("Inclinação (b):", b_quantidade)

# lineGraphic(dia, quantidade, ' ', a_quantidade, b_quantidade, ' ', ' ', 'Dia', 'Quantidade', ' ', ' ', ' ', ' ')

# a_quantidade, b_quantidade = regressaoLinear(dia, quantidade)
# print("\n---Quantidade---")
# print("Coeficientes de regressão linear para a componente de quantidade:")
# print("Interceptação (a):", a_quantidade)
# print("Inclinação (b):", b_quantidade)

# a_pensar, b_pensar = regressaoLinear(velocidade, pensar)
# print("---Pensar---")
# print("Coeficientes de regressão linear para a componente de pensar:")
# print("Interceptação (a):", a_pensar)
# print("Inclinação (b):", b_pensar)

# a_frear, b_frear = regressaoLinear(velocidade, frear)
# print("---Frear---")
# print("Coeficientes de regressão linear para a componente de frear:")
# print("Interceptação (a):", a_frear)
# print("Inclinação (b):", b_frear)

# mmq1Result = mmqGrau1(dia, quantidade)

# print("\n\na:", mmq1Result[0])
# print("b:", mmq1Result[1])

# mmq2Result = mmqGrau2(dia, quantidade)

# print("a:", mmq2Result[0])
# print("b:", mmq2Result[1])
# print("c:", mmq2Result[2])

# for estimatedDays in range(30, 42, 2):
#     estimated = mmq1Result[0] * estimatedDays + mmq1Result[1];
#     print(f"Estimativa de bactérias para {estimatedDays} dias é de {round(estimated,2)}.")
  
# print(f"A melhor equação g(x) = ax² + bx + c para prever a quantidade de bactéria após 30 dias é: {round(mmq2Result[0],2)} * x² + {round(mmq2Result[1],2)} * x + {round(mmq2Result[2],2)}")

# velocidade = [30, 45, 60, 75, 90, 120]
# pensar = [5.6, 8.5, 11.1, 14.5, 16.7, 22.4]
# frear = [5.0, 12.3, 21.0, 32.9, 47.6, 84.7]

# dispersalGraphic(velocidade, pensar, frear, 'Pensar', 'Frear', 'Velocidade (km/h)', 'Distância (m)')

# a_pensar, b_pensar = mmqGrau1(velocidade, pensar)
# print("\n---Pensar---")
# print("Coeficientes de regressão linear para a componente de pensar:")
# print("a:", a_pensar)
# print("b:", b_pensar)
# print("Equação de melhor ajuste é g(x) = ax + b: g(x), segue a equação: ", round(a_pensar, 4), "x + ", round(b_pensar, 4))

# a_frear, b_frear, c_frear = mmqGrau2(velocidade, frear)
# print("\n---Frear---")
# print("Coeficientes de regressão linear para a componente de frear:")
# print("a:", a_frear)
# print("b:", b_frear)
# print("c:", c_frear)
# print("Equação de melhor ajuste é g(x) = ax² + bx + c: g(x), segue a equação: ", round(a_frear, 4), "x² + ", round(b_frear, 4), "x + ", round(c_frear, 4))

# lineGraphic(velocidade, pensar, frear, a_pensar, b_pensar, a_frear, b_frear, 'Velocidade (km/h)', 'Distância (m)', 'Componente de Pensar', 'Componente de Frear', 'Regressão Linear de Pensar', 'Regressão Linear de Frear')

# carSpeed = 110

# thinkDistance = a_pensar * carSpeed + b_pensar

# brakeDistance = a_frear * carSpeed + b_frear

# print("\nEstimativa | Pensar:", round(thinkDistance, 2))
# print("Estimativa | Frear:", round(brakeDistance, 2))

# totalDistance = thinkDistance + brakeDistance

# print(f"Estimativa da distância para a parada total a {carSpeed} km/h é de {round(totalDistance, 2)} metros.")

# dia = [0, 4, 8, 12, 16, 20]
# quantidade = [67.38, 74.67, 82.74, 91.69, 101.60, 112.58]

# dispersalGraphic(dia, quantidade, ' ', 'Dia', 'Quantidade', ' ', ' ')
# a_quantidade, b_quantidade = mmqGrau1(dia, quantidade)

# lineGraphic(dia, quantidade, ' ', a_quantidade, b_quantidade, ' ', ' ', 'Dia', 'Quantidade', ' ', ' ', ' ', ' ')

# print("A equação de melhor ajuste pode ser g(x) = ax + b: g(x), segue a equação: ", round(a_quantidade, 4), "x + ", round(b_quantidade, 4))

# print("A equação de melhor ajuste é g(x) = a * x² + b * x + c", )
# x = np.array([1, 2, 3, 4, 5]) 
# y = np.array([0.5, 2, 2.9, 3.5, 4])

# xlog = np.log(x)
# print(xlog)

# result = mmqGrau2(x, y)
# print(result)

# print("a:", result[1])
# print("b:", result[2])
# print("c:", result[0])

# novoY = (np.log(2.6) * result[1]) - result[2]
# print("novoY:", novoY)

# velocidade = [30, 45, 60, 75, 90, 120]
# pensar = [5.6, 8.5, 11.1, 14.5, 16.7, 22.4]
# frear = [5.0, 12.3, 21.0, 32.9, 47.6, 84.7]

# dispersalGraphic(velocidade, pensar, frear, 'Pensar', 'Frear', 'Velocidade (km/h)', 'Distância (m)')

# a_pensar, b_pensar = mmqGrau1(velocidade, pensar)
# print("\n---Pensar---")
# print("Coeficientes de regressão linear para a componente de pensar:")
# print("a:", a_pensar)
# print("b:", b_pensar)
# print("Equação de melhor ajuste é g(x) = ax + b: g(x), segue a equação: ", round(a_pensar, 4), "x + ", round(b_pensar, 4))

# a_frear, b_frear = mmqGrau1(velocidade, frear)
# print("\n---Frear---")
# print("Coeficientes de regressão linear para a componente de frear:")
# print("a:", a_frear)
# print("b:", b_frear)
# print("Equação de melhor ajuste é g(x) = a * e ^(b * x), segue a equação: ", round(a_frear, 4), "* e ^ " , round(b_frear, 4), "* x")

# equacao = lambda x: a_frear * np.exp(b_frear * x)

# print(equacao(5.0))

# lineGraphic(velocidade, pensar, frear, a_pensar, b_pensar, equacao, 'Velocidade (km/h)', 'Distância (m)', 'Componente de Pensar', 'Componente de Frear', 'Regressão Linear de Pensar', 'Regressão Linear de Frear')

velocidade = [30, 45, 60, 75, 90, 120]
pensar = [5.6, 8.5, 11.1, 14.5, 16.7, 22.4]
frear = [5.0, 12.3, 21.0, 32.9, 47.6, 84.7]

dispersalGraphic(velocidade, pensar, frear, 'Pensar', 'Frear', 'Velocidade (km/h)', 'Distância (m)')

resultPensar = mmqGrau1(velocidade, pensar)
print("\n---Pensar---")
print("Coeficientes de regressão linear para a componente de pensar:")
print("a:", resultPensar[0])
print("b:", resultPensar[1])
print("Equação de melhor ajuste é g(x) = ax + b: g(x), segue a equação: ", round(resultPensar[0], 4), "x + ", round(resultPensar[1], 4))

resultFrear = mmqGrau2(velocidade, frear)
print("\n---Frear---")
print("Coeficientes de regressão linear para a componente de frear:")
print("a:", resultFrear[0])
print("b:", resultFrear[1])
print("c:", resultFrear[2])
print("A equação de melhor ajuste é g(x) = a * x² + b * x + c, segue a equação: ", round(resultFrear[0], 4), "* x² + ", round(resultFrear[1], 4), " * x ", round(resultFrear[2], 4))