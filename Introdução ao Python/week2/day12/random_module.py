'''
Módulo Random

OBS: Em python, módulos são nada mais que outros arquivos python.

-> O módulo random possui várias funções para geração de números pseudo-aleatórios

-> O módulo random é útil para se trabalhar com redes neurais
'''
print('\n')

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1: --> Importando o módulo diretamente

#import random as r

# Forma 2: --> Importando funções específicas do módulo utilizando 'from'

#from random import randint, random, randrange

# Podemos importar todas as funções utilizando asterisco (*)

from random import *

print(random()); print('\n') # a função random() gera números aleatórios entre 0 e 1

print(list(random() for i in range(10))); print('\n')

# Função uniform() -> Gera números pseudo-aleatórios entre os valores estabelecidos

print(list(uniform(3, 7) for i in range(10))) # O 7 não é incluido

print('\n')

print(list(randint(8, 19) for i in range(10)))
# A função randint(int, int) gera números inteiros entre o intervalo estabelecido

print('\n')

# Utilização do choice():

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas)); print('\n')

#========================================================================================================

# Imprimindo letras aleatórias

letras = 'qwertyuiopasdfghjklçzxcvbnm'
lista = []

for letra in letras:
    letra = letra.split()
    lista.append(letra[0])

print(choice(lista))