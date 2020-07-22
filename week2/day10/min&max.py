'''
Min & Max

min() -> Retorna o menor valor em um iterável
max() -> Retorna o maior valor em um iterável

'''
print('\n')

# >>>>>>>>>> Max <<<<<<<<<<

lista = [1, 5, 9, 18, 29, 33, 50, 90]
print(max(lista))

tupla = 1, 5, 9, 18, 29, 33, 50, 90
print(max(tupla))

mapa = {1, 5, 9, 18, 29, 33, 50, 90}
print(max(mapa))

dicionario = {'a':1, 'b':5, 'c':9, 'd':18, 'e':29, 'f':33, 'g':50, 'h':90}
print(max(dicionario.values())); print('\n')

#========================================================================================================

# Recebendo dois argumentos e informando qual dos dois é maior:

#val1 = int(input('Informe o primeiro valor: '))
#val2 = int(input('Informe o segundo valor: '))

val1 = 33
val2 = 42

print(f'Maior valor entre val1 e val2: {max(val1, val2)}'); print('\n')

# OBS --> O max() pode receber vários argumentos. Ele sempre retornará o maior valor dentre os...
#... argumentos passados

#========================================================================================================

# max() utilizando strings:

print(max('Felipe')) # Retorna a 'maior' letra de acordo com a ordem alfabética

print(max('abcyz')); print('\n')

#========================================================================================================

# >>>>>>>>>> Min <<<<<<<<<<

lista = [1, 5, 9, 18, 29, 33, 50, 90]
print(min(lista))

tupla = 1, 5, 9, 18, 29, 33, 50, 90
print(min(tupla))

mapa = {1, 5, 9, 18, 29, 33, 50, 90}
print(min(mapa))

dicionario = {'a':1, 'b':5, 'c':9, 'd':18, 'e':29, 'f':33, 'g':50, 'h':90}
print(min(dicionario.values())); print('\n')

#========================================================================================================

# Recebendo dois argumentos e informando qual dos dois é menor:

#val1 = int(input('Informe o primeiro valor: '))
#val2 = int(input('Informe o segundo valor: '))

val1 = 33
val2 = 42

print(f'Menor valor entre val1 e val2: {min(val1, val2)}'); print('\n')

# OBS --> O min() pode receber vários argumentos. Ele sempre retornará o menor valor dentre os...
#... argumentos passados

#========================================================================================================

# min() utilizando strings:

print(min('felipe')) # Retorna a 'menor' letra de acordo com a ordem alfabética

print(min('bcayz'))

print(min('Felipe Ribeiro')) # Nesse caso, o espaço entre as strings é considerado como o 'menor' valor
# Por isso nem é mostrado no terminal

#========================================================================================================
print('\n')

# ------> Mais exemplos utilizando min() e max() <------

nomes = ['Felipe', 'Camila', 'Antônio', 'Sarah', 'Eduardo', 'Max', 'Olivander']

print(max(nomes)) # Retorna o maior NÃO pelo tamanho, mas sim pela ordem alfabética
print(min(nomes)) # Retorna o menor NÃO pelo tamanho, mas sim pela ordem alfabética

# Dessa forma retorna pelo TAMANHO da string:
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome))); print('\n')

#========================================================================================================

musicas = [
    {'música': 'Again', 'tocou': 3},
    {'música': 'Touch off', 'tocou': 1},
    {'música': 'Ignite', 'tocou': 7},
    {'música': 'The Day', 'tocou': 2}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprimindo apenas o título da mais e da menos tocada:
print(max(musicas, key=lambda musica: musica['tocou'])['música'])
print(min(musicas, key=lambda musica: musica['tocou'])['música'])