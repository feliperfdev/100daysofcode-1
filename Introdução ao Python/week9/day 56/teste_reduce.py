from math import *
from functools import reduce

'''
Olhar week2 day 8 para ver o conteúdo sobre reduce
'''

soma = lambda x, y: x+y
lista = [30, 45, 60, 90, 120]

calculaSeno = reduce(soma, lista)

print(calculaSeno)

#=============================================================================

def somaElementosLista(lista):
    soma = lambda x,y: x+y
    res = reduce(soma, lista)
    print(res)

somaElementosLista([1, 2, 3, 4])

#=============================================================================