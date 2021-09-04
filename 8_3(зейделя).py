from math import sqrt
import numpy as np
from numpy import array


A = array([[24,-7,-4,4],[-3,-9,-2,-2],[3,7,24,9],[1,-6,-2,-15]])

b = array([-190,-12,155,-17])
m = len(A)
x = [.0 for i in range(m)]
Iteration = 0
converge = False
pogr = 0.
while not converge:
    x_new = np.copy(x)
    for i in range(m):
        s1 = sum(A[i][j] * x_new[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
        x_new[i] = (b[i] - s2 - s1) / A[i][i]
    pogr = sum(abs(x_new[i] - x[i]) for i in range(m))
    converge = pogr < 1e-6
    Iteration += 1
    x = x_new
print('Количество итераций :', Iteration)
print('Решение системы уравнений :', x)
print('Погрешность :', pogr)
