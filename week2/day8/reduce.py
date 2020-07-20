'''
Reduce --> Módulo functools

--> 99% das vezes, é mais legível utilizar o loop for ao invés do reduce() -- Dito pelo prórpio criador
do python

'''
print('\n')

'''
Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

E tem também uma função:

def função(x, y):
    return x*y

Assim como map() e filter(), o reduce() recebe dois parâmetros --> (função, iterável qualquer)

reduce(função, dados)

Como funciona o reduce():
    Passo 1: res1 = f(a1, a2) --> Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) --> Aplica a função passando o resultado do res1 e o terceiro elemento
da coleção e guarda o resultado
    Passo 3: res3 = (res2, a4)
    .
    .
    .
    Passo n: resn = (resn-1, an)

Basicamente, o reduce é como: função(função(função((a1, a2), a3), a4), ...), an)
'''

# Na prática:

from functools import reduce

dados = [1, 3, 5, 11]

# Para utilizar o reduce(), precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x*y

res = reduce(multi, dados)
print(res)

# o que aconteceu: 1*3 = 3 // 3*5 = 15 // 15*11 = 165

# Outro exemplo:
outros_dados = [1, 2, 4, 6, 8]
multi_novamente = lambda x1, y1: x1*y1

res1 = reduce(multi_novamente, outros_dados)
print(res1); print('\n') # 1*2 = 2 // 2*4 = 8 // 8*6 = 48 // 48*8 = 384

# ---> É como se utilizasse a lógica de recursividade

# Utilizando loop for:      ----> Mais fácil de perceber a recursividade <----

res_for = 1
for n in dados:
    res_for = res_for*n

print(res_for)

res_for2 = 1
for n in outros_dados:
    res_for2 = res_for2*n

print(res_for2)