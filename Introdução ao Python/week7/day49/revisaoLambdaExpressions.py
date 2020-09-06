from math import *
from statistics import *

print()
print('{:=^77}'.format('REVISÃO LAMBDA'))

sumThreeNumbers = lambda x, y, z: x+y+z
# cria uma função 'sumThreeNumbers' e ela recebe 3 parâmetros

print(sumThreeNumbers(1, 4, 7))

listaF = [5, 6, 7, 8]
realizaFatorial = list(map(lambda x: factorial(x), listaF))
# A função dessa vez não recebe parâmetros, mas ela aplica a função factorial() a todos os
# elementos contidos em 'listaF'
print(realizaFatorial)

# Entendendo a síntaxe do lambda

'''

O lambda é escrito dessa forma --->     lambda variavel: alguma_ação_na_variavel

A variável informada antes dos ':' é como uma 'variável de suporte'
Ou seja, essa variável irá ser relacionada a uma ação em um determinado objeto ou iterável
para poder realizar a função

No exemplo anterior, utilizei o map() para realizar uma função auxiliada pelo lambda em uma lista
No caso, a variável de suporte do lambda foi informada para a função factorial(), ou seja, o x
será relacionado a cada um dos elementos da lista e, então, a função factorial() será aplicada
em cada um desses elementos.

'''

# Entendendo isso:

calculaSenoLista = list(map(lambda x: sin(x), [30, 60, 90]))
# Basicamente, estou utilizando o map() para, através do lambda, gerar uma variável de suporte
# que será aplicada à função sin(). Logo após, essa variável irá se relacionar (ITERAR) 
# aos 3 elementos da lista informada e aplicará a função sin() em cada um deles.

print(calculaSenoLista)

# Outro exemplo:

# calculaMediaLista = list(map(lambda x: mean(x), [5, 5, 7, 1, 2]))
# Nesse caso, não haverá o funcionamento. Pois o lambda, como havia dito, utiliza a variável
# de suporte para ITERAR em cada um dos elementos do iterável informado. Entretanto, a função
# mean() não funciona iterando sobre os elementos de um iterável, mas sim realizando uma
# determinada OPERAÇÃO em um iterável

# print(calculaMediaLista)

# Ou seja, existem funções em que nem sempre será possível iterar com expressões lambda

# Calculando a média da maneira certa:

calculaMediaSemLambda = mean([5, 5, 7, 1, 2])
print(f'Média: {calculaMediaSemLambda}')

# ============== Expressão mabda com parâmetro padrão: ===============

expLambdaParamPadrao = lambda x=0, y=0: x*y

print(expLambdaParamPadrao(3, 4))
print(expLambdaParamPadrao())

# ====================================================================