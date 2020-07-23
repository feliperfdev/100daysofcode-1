'''
Listas Aninhadas

-> Linguagens como C/Java possuem uma estrutura de dados chamada array:
        - Unidimensionais (arrays/vetores)
        - Multidimensionais (matrizes)

-> Em Python temos as listas
'''
print('\n')

# Exemplo:

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(type(lista))
print(lista)

print('\n'); print(lista[0]) # Acessa a primeira lista

print('\n'); print(lista[0][1]) # Acessa o elemento '2' da primeira lista

print(lista[1][2])
print(lista[2][0]); print('\n')

[[print(valor, end=' ') for valor in listas] for listas in lista]; print('\n')

[[print(elemento*2, end=' ') for elemento in listas_] for listas_ in lista]

#==========================================================================================================
print('\n')

matriz = [[num for num in range(1, 4)] for value in range(1, 4)]
print(matriz)

print('\n'); import numpy as np

matriz_array = np.array(matriz)
print(matriz_array)

#==========================================================================================================
print('\n')

velha = [['x' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]

jogo_da_velha = np.array(velha)
print(jogo_da_velha)