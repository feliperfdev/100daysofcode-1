'''
Módulos Built-in --> Módulos integrados da instalação do Python

OBS: Já vêm instaladas, porém não se inicializam com ele

Lista de módulos built-in -> {https://docs.python.org/3/py-modindex.html}

'''
print('\n')

# Funções que já vem instaladas ao Python e se inicializam com ele:

print(dir(__builtins__))

# Podemos dar 'apelidos' aos módulos

import random as rd

print(rd.randint(3, 7))

# Podemos importar todas as funções de um módulo utilizando asterísco (*)

from random import *

print(randint(3, 7))

# Apelidando as funções do módulo

from random import randint as rdi

print(rdi(1, 9))

# Importando mais de uma função

from random import random, randint

from random import (choice, 
randint, 
shuffle, 
seed, 
expovariate)

