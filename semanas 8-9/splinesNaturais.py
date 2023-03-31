import numpy as np


def splinesNaturais(numberPoints, vetorAbscissasOrdemCrescente, vetorOrdenadas):
    # Criação da matriz A
    matrizA = np.zeros((numberPoints, numberPoints))
    matrizA[0, 0] = 1
    matrizA[numberPoints - 1, numberPoints - 1] = 1
    for i in range(1, numberPoints - 1):
        matrizA[i, i - 1] = vetorAbscissasOrdemCrescente[i] - vetorAbscissasOrdemCrescente[i - 1]
        matrizA[i, i] = 2 * (vetorAbscissasOrdemCrescente[i + 1] - vetorAbscissasOrdemCrescente[i - 1])
        matrizA[i, i + 1] = vetorAbscissasOrdemCrescente[i + 1] - vetorAbscissasOrdemCrescente[i]
    # Criação do vetor b
    vetorB = np.zeros(numberPoints)
    for i in range(1, numberPoints - 1):
        vetorB[i] = 3 * ((vetorOrdenadas[i + 1] - vetorOrdenadas[i]) / (vetorAbscissasOrdemCrescente[i + 1] - vetorAbscissasOrdemCrescente[i]) - (vetorOrdenadas[i] - vetorOrdenadas[i - 1]) / (vetorAbscissasOrdemCrescente[i] - vetorAbscissasOrdemCrescente[i - 1]))
    # Resolução do sistema
    vetorC = np.linalg.solve(matrizA, vetorB)
    # Criação dos vetores a, b e d
    vetorA = np.zeros(numberPoints)
    vetorB = np.zeros(numberPoints)
    vetorD = np.zeros(numberPoints)
    for i in range(0, numberPoints - 1):
        vetorA[i] = vetorOrdenadas[i]
        vetorB[i] = (vetorOrdenadas[i + 1] - vetorOrdenadas[i]) / (vetorAbscissasOrdemCrescente[i + 1] - vetorAbscissasOrdemCrescente[i]) - (2 * vetorC[i] + vetorC[i + 1]) * (vetorAbscissasOrdemCrescente[i + 1] - vetorAbscissasOrdemCrescente[i]) / 3
        
    return vetorA, vetorB, vetorC, vetorD


