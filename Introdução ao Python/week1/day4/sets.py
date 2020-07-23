"""
Conjuntos --> Sets

-> Faz-se referência à Teoria Matemática dos Conjuntos

- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Sets não são indexados
- Sets são mutáveis

-> Conjuntos são utilizados quando precisamos armazenar elementos, mas sem se importar com a
ordenação deles. Ou seja, sem se preocupar com chaves e valores.

-> Sets são referenciados com chaves {}. Então qual é a diferença entre sets e dicionários?
            - Dicionários possuem chaves/valores
            - Sets possuem apenas valores


"""

print('\n')

# Definindo um set:

# Forma 1:

s = {1, 2, 3, 4}
print(type(s))
print(s)

print('\n')
# Forma 2:

s2 = set({1, 2, 3, 4, 5})
print(type(s2))
print(s2)

#==========================================================================================================
print('\n')

# Não podemos repetir valores:

s1 = {1, 2, 3, 1, 1, 2}
print(s1) # Ele elimina os valores repetidos

s_2 = set({1, 2, 3, 4, 4, 4, 5, 6, 6, 1})
print(s_2) # Ele elimina os valores repetidos

#==========================================================================================================
print('\n')

lista = [1, 2, 3, 3, 3, 4, 4, 1, 5, 6, 2, 7, 7]
s_lista = set(lista)
print(s_lista) # Ele elimina os valores que repetiram na lista

tupla = (1, 1, 2, 3, 4, 5, 2, 5, 'teste', 'aaa', 'teste', 3, 2, 4)
s_tupla = set(tupla)
print(s_tupla)

dicionario = {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 3, 'f': 4, 'g': 3}
s_dict = set(dicionario.values()) #Acessando apenas os valores do dicionário e os colocando dentro do set
print(s_dict) # Ocorreu o mesmo. Foram eliminados os valores que repetiram

# Como nos dicionários, por convenção, não pode haver repetição de CHAVES, não precisamos nos...
#... preocupar com elas. Apenas com os valores.

dicionario_2 = {}.fromkeys([1, 2, 3, 3, 'opa', 4, 5, 6, 6, 'opa', 4], 'dict')
s_dict2 = set(dicionario_2)
print(s_dict2)
# Por convenção do set, o valor ('dict') já não seria mostrado

# O set ignora os valores repetidos independente do tipo de dado

#==========================================================================================================
print('\n')

# Usos interessantes com sets:

'''Imagine que fizemos uma lista de cadastro de visitantes de um museu e os visitantes informam manualmente
as cidades de onde vieram'''

'''Nós adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar elementos e
ter repetições'''

cidade = ['Salvador', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo', 'Salvador', 'São Paulo']
print(cidade)
print('Quantidade informada: ', len(cidade))

'''O que fariamos para saber quantas cidade distintas (únicas) têm na lista?'''
print('Cidades únicas: ', len(set(cidade)))

#==========================================================================================================
print('\n')

# Adicionando elementos em um set:

conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.add(6)
print(conjunto)

conjunto.add(6) # Tentando adicionar um valor já existente
print(conjunto) # Ele ignora essa adição

#==========================================================================================================
print('\n')

# Removendo elementos em um set:

conjunto = {1, 2, 3, 4, 5}

# Forma 1:

conjunto.remove(3) # Remove por elemento, NÃO por índice

# Forma 2:

conjunto.pop()
print(conjunto) # Remove o PRIMEIRO elemento

# Forma 3:

conjunto.discard(4)
print(conjunto)

#==========================================================================================================
print('\n')

# Copiando um conjunto para outro: DeepCopy & ShallowCopy

# DeepCopy:

s_et = {1, 2, 3}

novo = s_et.copy()
print(novo)

novo.add(4)
print(novo)
print(s_et) # Não altera seus valores originais

# ShallowCopy:

novo = s

s.add(5) #Está adicionando em ambos
print(novo)
print(s)

#==========================================================================================================
print('\n')

# Podemos remover todos os items de um set:

s0  = {1, 2, 3}
print(s0)
s0.clear()
print(s0)

#==========================================================================================================
print('\n')

# Aplicações matemáticas com set:

estudantes_python = {'Felipe', 'João', 'Júlia', 'Cesar', 'Amanda', 'Pedro'}
estudantes_c = {'Felipe', 'Marcos', 'Júlia', 'André', 'Eduarda', 'Rafael', 'João'}

print(estudantes_python)
print(estudantes_c); print('\n')

# >>>>>>>>>> Unindo dados dos dois conjuntos <<<<<<<<<<

# Forma 1: --> Utilizando union()     Mais recomendado

uniao1 = estudantes_python.union(estudantes_c)
print(uniao1)

# Forma 2: --> utilizando o pipe |

uniao2 = estudantes_python | estudantes_c
print(uniao2)

print('\n')
# >>>>>>>>>>> Interseção de dados dos dois conjuntos <<<<<<<<<

# Forma 1: --> Utilizando o intersection()      Mais recomendado

inters = estudantes_python.intersection(estudantes_c)
print(inters)

# Forma 2: --> Utilizando o 'e' comercial &

inters2 = estudantes_c & estudantes_python
print(inters2)

print('\n')
# >>>>>>>>>> Diferença: Estudantes que estão em um único curso <<<<<<<<

# --> Utilizando o difference()

difer = estudantes_python.difference(estudantes_c)
print(difer)

difer2 = estudantes_c.difference(estudantes_python)
print(difer2)

#==========================================================================================================
print('\n')

conjunto1 = {1, 2, 3}

print(sum(conjunto1))
print(max(conjunto1))
print(min(conjunto1))
print(len(conjunto1))