''''
Generators --> Seria um tipo de 'tuple comprehension'



'''
print('\n')

nomes = ['Carlos', 'Cleber', 'Claudia', 'Cesar', 'Camlila', 'Felipe']

# List Comprehension:
print([nome[0]=='C' for nome in nomes]); print('\n') # --> True
lista_nomes = [nome[0]=='C' for nome in nomes]

# Generator ------> Ocupa menos recursos e menos memória
print(nome[0]=='C' for nome in nomes) # --> True
gen_nomes = (nome[0]=='C' for nome in nomes)
print(type(gen_nomes))

from sys import getsizeof # retorna a quantidade de bytes do elemento usado como argumento

print(getsizeof(gen_nomes)) # -> Generator: 112
print(getsizeof(lista_nomes)) # -> List Comprehension: 120

print('\n')
#========================================================================================================

# Gerando uma lista de números utilizando List Comprehension:
list_comp = getsizeof([x*10 for x in range(1000)])

# Gerando uma lista de números utilizando Set Comprehension:
set_comp = getsizeof({x*10 for x in range(1000)})

# Gerando uma lista de números utilizando Dictionary Comprehension:
dict_comp = getsizeof({x: x*10 for x in range(1000)})

# Gerando uma lista de números utilizando Generator Expression:
gen_expression = getsizeof(x*10 for x in range(1000))

print('Para realizar uma mesma tarefa, gastamos utilizando: \n')

print(f'List comprehension: {list_comp} bytes') # --> 9016 bytes
print(f'Set comprehension: {set_comp} bytes') # --> 32984 bytes
print(f'Dictionary comprehension: {dict_comp} bytes') # --> 36960 bytes
print(f'Generator expression: {gen_expression} bytes') # --> 112 bytes

'''
Por quê isso acontece?

-> Tanto no list comprehension, quanto no set e dict comprehension, os valores são gerados e guardados
na memória naquele momento

-> O generator não gera os valores automaticamente. Ele só gera quando precisarmos utilizar.

'''
print('\n')
#========================================================================================================

# Iterando no Generator Expression:

gen = (num * 10 for num in range (10))

print([numero for numero in gen]); print('\n')

# Veja como a memória no Generator Expression é drasticamente reduzida em comparação aos comprehensions:

# Utilizando any e all no Generator Expression

gen2 = (num for num in [0, 2, 4, 6, 8, 10] if num%2==0)

print(any(numero for numero in gen2))
print(all(numero for numero in gen2))

print(getsizeof(gen2)) # 112 bytes
print(getsizeof(all(numero for numero in gen2))) # 28 bytes

#========================================================================================================
print('\n')

# Mais exemplos utilizando Generator Expression:

from math import sin, cos, tan

numeros = [30, 60, 90, 120, 180, 270]

gen_numeros = (num for num in numeros)
print(gen_numeros)
print(getsizeof(gen_numeros)); print('\n')

print(list(map(lambda dado: sin(dado), gen_numeros)))
print(f'{getsizeof(list(map(lambda dado: sin(dado), gen_numeros)))} bytes')