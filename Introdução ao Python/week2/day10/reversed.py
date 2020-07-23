'''
Reversed

--> Não confundir com a função .reverse() da lista

'''
print('\n')

# A função .reverse() só funciona nas listas

lista = [1, 2, 3, 4, 5, 6]
lista.reverse()
print(lista); print('\n')

#========================================================================================================

# A função reversed() funciona com QUALQUER iterável. Ele basicamente inverte o iterável.

lista_2 = [1, 2, 3, 4, 5, 6]
res = reversed(lista_2)
print(res) # O reversed() retorna um objeto do tipo 'reverseiterator'

# Convertendo o objeto retornado para lista, tupla ou set:

print(list(reversed(lista_2)))
print(tuple(reversed(lista_2)))
print(set(reversed(lista_2))) # Pq o set não inverteu? Lembre-se: O set, por convenção, não possui ordem

print('\n')
#========================================================================================================

# Iterando no reversed:

for letra in reversed('Felipe Ribeiro'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o 'for':

print(''.join(reversed('Felipe Ribeiro')))

# Invertendo strings utilizando o slice de strings:

print('Felipe Ribeiro'[::-1]); print('\n')

#========================================================================================================

for n in reversed(range(0, 10)):
    print(n, end=' ')

print('\n')
# Podemos fazer o mesmo da seguinte forma:

for n in range(9, -1, -1):
    print(n, end=' ')