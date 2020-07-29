'''
Entendendo Iteratores (Iterator) e Iteráveis

Iterador ->
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterável ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada
Exemplos de iteráveis: Strings, listas, tuplas, dicionários, sets...

'''
print('\n')

nome = 'Felipe' # É um iterável mas não é um iterator
num = [1, 3, 5, 7, 9] # É um iterável mas não é um iterator

'''
print(next(nome))
print(next(num))
'''
# Vai dar erro nos dois pq nenhum é iterador

itnome = iter(nome)
itnum = iter(num)

print(next(itnome)) # F
print(next(itnome)) # E
print(next(itnome)) # L
print(next(itnome)) # I
print(next(itnome)) # P
print(next(itnome)) # E

print('\n')

print(next(itnum)) # 1
print(next(itnum)) # 3
print(next(itnum)) # 5
print(next(itnum)) # 7
print(next(itnum)) # 9

print('\n')
# Maneira clássica de iterar:

for letra in nome:
    print(letra)