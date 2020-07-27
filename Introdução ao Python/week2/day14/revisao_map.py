print('\n')

from math import factorial

lista = [1, 2, 3, 4, 5, 6]

print(list(map(lambda num: factorial(num), lista)))

print('\n')
#========================================================================================================

nome = 'Felipe', 'Eduador', 'Camila', 'Larissa', 'Cesar', 'Bruna'

print(list(map(lambda name: name.split(), filter(lambda name: name[-1]=='a', nome))))

print('\n')
#========================================================================================================

numeros = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

print(list(map(lambda num: factorial(num), filter(lambda num: num>10, numeros))))

print('\n')
#========================================================================================================


