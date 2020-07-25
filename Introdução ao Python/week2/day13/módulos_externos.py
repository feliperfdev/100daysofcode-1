'''
Módulos Externos

Abrir o cmd (command prompt) -> pip install pacote

pip = python installer  package


'''
print('\n')

import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array = np.array(matriz)
print(array); print('\n')

print(np.ones(5)); print('\n')

print(np.ones((5, 5))); print('\n')

print(np.ones((3, 3), order='F')); print('\n')

print(np.zeros((4, 4))); print('\n')

a1 = np.array(numeros)

print(a1); print('\n')

print(np.repeat(3, 7))