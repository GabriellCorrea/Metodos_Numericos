import numpy as np

def eliminacao_gauss(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    for i in range(n):
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            A[j] = A[j] - fator * A[i]
            b[j] = b[j] - fator * b[i]

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        soma = np.dot(A[i][i + 1:], x[i + 1:])
        x[i] = (b[i] - soma) / A[i][i]

    return x