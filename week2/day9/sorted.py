'''
Sorted --> Função sorted()

-> Função integrada do Python

OBS: Não confunda, apesar do nome, com a função .sort()

--> O .sort() funciona APENAS com LISTAS

--> O sorted() funciona com QUALQUER iterável, incluindo listas.

'''
print('\n')

lista = [1, 9, 8, 4, 6]
lista.sort()
print(lista)

print(sorted(lista)); print('\n')

# Na lista, qual a diferença do sorted() para o .sort()?
# -> O .sort() modifica a lista, ou seja, a mudança feita nela (ordenação) é permanente
# -> No sorted() é criado uma nova lista aplicando a função de ordenação, mas a lista original não é...
# ... modificada
#========================================================================================================

tupla = (6, 1, 8, 34, 5, 2, 7, 15)
print(f'Tupla: {tupla}')
print(f'Tupla ordenada: {sorted(tupla)}') # Gera uma lista
print(f'Tupla ordenada: {tuple(sorted(tupla))}'); print('\n')

# OBS: Não importa o objeto que seja passado como argumento para o sorted(), ele sempre retornará
#... uma lista

set_ = {9, 56, 3, 78, 33, 86, 6, 2, 45, 1}
print(f'Set: {set_}')
print(f'Set ordenado: {sorted(set_)}') # Gera uma lista
print(f'Set ordenado: {set(sorted(set_))}'); print('\n')

#========================================================================================================

# Adicionando parâmetros ao sorted():

numeros = [3, 4, 6, 7, 1, 9, 33, 8, 0, 23, 2]

print(f'Ordem crescente: {sorted(numeros)}')
print(f'Ordem decrescente: {sorted(numeros, reverse=True)}') # Ordenação reversa

#========================================================================================================
print('\n')

usuarios = [
    {'username': 'Felipe', 'tweets': ['Programo em Python', 'Eu gosto de pizza'], 'cor': 'verde', 
                                                                                        'idade': 18},
    {'username': 'Carlos', 'tweets': ['Programo em Javascript'], 'idade': 15},
    {'username': 'Julia', 'tweets': [], 'cor': 'amarelo', 'idade': 17},
    {'username': 'Cesar', 'tweets': [], 'idade': 20},
    {'username': 'Camila', 'tweets': ['Programo em Java', 'Eu gosto de coxinha'], 'idade': 18}
]

print(sorted(usuarios, key=len)); print('\n') # Ordena pelo tamanho
print(sorted(usuarios, key=lambda user: user['username'])) # Ordena por ordem alfabética do username
print('\n'); print(sorted(usuarios, key=lambda tts: len(tts['tweets']))) # Ordena pela quantidade...
#... de tweets ---> Menor para maior quantidade
print('\n'); print(sorted(usuarios, key=lambda tts: len(tts['tweets']), reverse=True)) # Ordena pela... 
# quantidade de tweets ---> Maior para menor quantidade
print('\n'); print(sorted(usuarios, key=lambda idade: idade['idade'])) # Ordena pela idade

print('\n')
#========================================================================================================

# Mais um exemplo:

musicas = [
    {'música': 'Again', 'tocou': 3},
    {'música': 'Touch off', 'tocou': 1},
    {'música': 'Ignite', 'tocou': 7},
    {'música': 'The Day', 'tocou': 2}
]

# Ordena da música menos tocada para a mais tocada:
print(sorted(musicas, key=lambda music: music['tocou']))

# Ordena da música mais tocada para a menos tocada:
print(sorted(musicas, key=lambda music: music['tocou'], reverse=True))

# Ordena por ordem alfabética:
print(sorted(musicas, key=lambda music: music['música']))