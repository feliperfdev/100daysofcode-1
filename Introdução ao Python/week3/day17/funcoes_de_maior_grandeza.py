'''
Funções de Maior Grandeza - High Order Functions (HOF)

O que isso significa?
    -> Quando uma linguagem de programação suporta/permite o HOF, indica que podemos ter funções
que retornam outras funções como resultado, ou mesmo que podemos passar funções como argumento para
outras funções, e até mesmo criar variáveis do tipo de funções.

OBS: 
'''
print('\n')

# Exemplo - Definindo funções

def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

print('\n')
#======================================================================================================

# Nested Functions (Funções Aninhadas) --> Funções dentro de funções

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(['feliz', 'triste', 'chateado'])
    return pessoa + ' ' + humor()

print(cumprimento('Felipe'))

#======================================================================================================

print('\n')

def risada():
    def rir():
        return choice(['kkkkkkkkkkk', 'rsrsrsrs', 'hahahahaha'])
    return rir()

print(risada())

#======================================================================================================