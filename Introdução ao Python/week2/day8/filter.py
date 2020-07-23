'''
Filter --> filter()

-> A função filter serve para filtrar dados de uma determinada coleção

'''
print('\n')

valores = 1, 2, 3, 4, 5, 6

def media(val):
    return sum(val) / len(val)

print(media(valores)); print('\n')

#=========================================================================================================

import statistics as st # Biblioteca para trabalhar com dados estatísticos

# >>>>>>>>>>> Exemplos <<<<<<<<<<

# Dados coletados de algum sensor:

dados = [1.3, 2.7, 0.9, 3.2, -8.5, 4.1]

calcula_media = st.mean(dados) # st.mean() --> cálcula média

# OBS: Assim como a função map(), a filter() também recebe dois argumentos --> (função, iterável qualquer)

print(f'Média dos dados: {calcula_media}')

print(list(filter(lambda valor: valor>calcula_media, dados))); print('\n')
# Filtra apenas os valores que estão acima da média

# Assim como na função map(), os dados de filter() são excluidos da memória após serem utilizados

#=========================================================================================================

# filter() também é utilizado na análise e remoção de dados ausentes

paises = ['', 'Brasil', 'Argentina', '', 'Japão', 'Espanha', '', '']

print(list(filter(None, paises))) # Passando o tipo None como argumento, ele filtra os dados vazios...
#... no iterável 'países'

# Outra forma:
print(list(filter(lambda pais: len(pais) > 0, paises))) # Ele utiliza a função len() para pegar o...
#... tamanho da palavra que compõe cada país. Portanto, qualquer dado no iterável 'paísese' que...
#... apresente tamanho menor que zero, será filtrado. Então, serão retornados como valores apenas...
#... os dados que possuem tamanho maior que zero dentro deste iterável.

# Outra forma:
print(list(filter(lambda pais: pais != '', paises))) # Não é muito recomendado fazer dessa maneira

print('\n')
#=========================================================================================================

# >>> A diferença entre map() e filter() é que: <<<
# -> Na map() é retornado um objeto que mapeia a função para cada elemento de um iterável qualquer
# -> Na filter() é retornado um objeto filtrando apenas os elementos de acordo com a função

#=========================================================================================================

# Mais exemplos:

usuarios = [
    {'username': 'Felipe', 'tweets': ['Programo em Python', 'Eu gosto de pizza']},
    {'username': 'Carlos', 'tweets': ['Programo em Javascript']},
    {'username': 'Julia', 'tweets': []},
    {'username': 'Cesar', 'tweets': []},
    {'username': 'Camila', 'tweets': ['Programo em Java', 'Eu gosto de coxinha']}
]

print(usuarios); print('\n')

# Filtrando usuários inativos

print(list(filter(lambda user: len(user['tweets'])==0, usuarios)))

# Outra forma:
print(list(filter(lambda user: not user['tweets'], usuarios)))

# utilizar a palavra reservada 'not' para tratar de dados booleanos. Ou seja, nesse caso, ...
# ... é como se pedissemos para apenas filtrar as listas que retornem o booleano False...
# ... ou seja, as listas vazias

#=========================================================================================================

# OBS: --> Lembrar que uma lista vazia, quando analisada em booleano, irá retornar False...
#... já listas com dados dentro, analisadas em booleano, retornarão Truee

lista = [1, 2, 3]
lista_vazia = []

print(bool(lista)) # --> True
print(bool(lista_vazia)) # --> False

print('\n')
#=========================================================================================================

# Combinando filter() e map():

professores = ['André', 'Marco', 'Ronaldo']

# Devemos criar uma lista contendo 'Seu instrutor é' +  professores // desde que cada nome de professor...
#... tenha menos de 5 caracteres ou exatos 5 caracteres

print(list(map(lambda nome: f'Seu instrutor é: {nome}', filter(lambda name: len(name)<=5, professores))))
#            [tudo isso é o primeiro argumento do map]         [1º argumento filter]    [2º arg. filter]
#                                                       [   tudo isso é o segundo argumento do map     ]
#                                                       [               iterável filtrado              ]
print('\n')

# Basicamente, o que aconteceu no print() anterior:
print(list(filter(lambda nome: len(nome)<=5, professores))) # retorna --> ['André', 'Marco']
print(list(map(lambda nome: f'Seu instrutor é: {nome}', ['André', 'Marco'])))
# Perceba que nesse segundo print foi passado como segundo parâmetro do map o retorno do primeiro print

# Por isso podemos fazer: 
# map(lambda nome: f'Seu instrutor é: {nome}', filter(lambda nome: len(nome)<=5, professores))
# [                 1                    ]     [                      2                      ]
#=========================================================================================================