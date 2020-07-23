""""
Dictionaries (dict)

-> Em outras linguagens os dicionários podem ser chamados de 'mapas'

-> Dicionários são coleções do tipo chave/valor --> {chave:valor}
-> São representados por chaves {}
-> Tanto chaves quanto os valores podem ser de quaisquer tipos de dados
-> Dicionários não são indexados

-> Não se pode repetir chaves de mesmo nome dentro de um único dicionário

-> 

"""
print("\n")

#Formar de representação

# -> Mais comum:
paises = {'br': 'Brasil', 'eua': 'United States'}
print(type(paises))

# -> Menos comum:

countries = dict(br='Brasil', eua='United States')
print(type(countries))

#=================================================================================================================
print("\n")
# Acessando elementos:

print(paises['br']) #Acessamos os valores através das chaves
print(paises['eua'])
#print(countries['nao_existe']) #Erro

print("\n")
# Acessando elementos utilizando o get(): --> Recomendado!!!

print(paises.get('br'))
print(countries.get('nao_existe')) #Não dá ero, ao invés disso, retorna o tipo None

print("\n")
#=================================================================================================================

paises = {'br': 'Brasil', 'eua': 'United States', 'jp': 'Japão'}

russia = paises.get('ru') # None --> False
japao = paises.get('jp')

if japao:
    print(f'Encontrei o país {japao}')
else:
    print(f'Não encontrei o país')

print("\n")

if russia:
    print(f'Encontrei o país {russia}')
else:
    print(f'Não encontrei o país')

#=================================================================================================================
print("\n")

paises = {'br': 'Brasil', 'eua': 'United States', 'jp': 'Japão', 'kor': 'Coreia'}

coreia = paises.get('kor', 'Não encontrado')
#O que significa: Se encontrar a chave 'kor', ele vai retornar o valor. Caso não encontre, ...
#... ele vai retornar o 'Não encontrado'

#Assim não precisaremos mais do condicional if

print(f'{coreia}')

print("\n")
paises_1 = {'br': 'Brasil', 'eua': 'United States', 'jp': 'Japão'}

coreia_1 = paises_1.get('kor', 'Não encontrado')

print(f'{coreia_1}')

#=================================================================================================================
print("\n")

paises = {'br': 'Brasil', 'eua': 'United States', 'jp': 'Japão', 'kor': 'Coreia'}

#Podemos verificar se existe uma determinada chave no dicionário:

print('br' in paises)
print('eua' in paises)
print('abc' in paises)

#=================================================================================================================
print("\n")

localidade = { # Tuplas sendo utilizadas como chaves de dicionários
    (13.43937, 78.95372): 'Japão',
    (112.3483, 91.09949): 'Coréia do Sul',
    (33.38019, 87.14377): 'Brasil'
}       # --> Coordenadas de valores irreais

#=================================================================================================================
print("\n")

#Adicionando elementos no dicionário:

receita = {'jan': 100, 'fev': 150, 'mar': 200}
print(receita); print("\n")

# Forma 1: --> Mais comum

receita['abr'] = 250
print(receita); print("\n")

# Forma 2:

novo_valor = {'mai': 300}
receita.update(novo_valor)
print(receita); print("\n")

att_fev = {'fev': 180}
receita.update(att_fev)
print(receita)

# O update() serve tanto para adicionar novos dados como também para atualizar os dados...
#... de chaves já existentes no dicionário

receita.update({'mar': 240})
print(receita)

receita['jan'] = 125
print(receita)

print("\n")

# Removendo elementos de um dicionário

# Forma 1:

receita.pop('mar')
print(receita)

ret = receita.pop('abr')
print(ret) #Remove e retorna o valor que foi removido
print(receita)

print("\n")
# Forma 2: --> Utilizando: del dicionário['chave']

paises = {'br': 'Brasil', 'eua': 'United States', 'jp': 'Japão', 'kor': 'Coreia'}
print(paises)
                    # O valor removido não é retornado, apenas removido e pronto
del paises['eua']
print(paises)

#=================================================================================================================
print('\n')

# Onde/quando utilizamos dicionários?

'''Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos...
produtos nele'''

'''Carrinho de compras:

        Produto 1: 
            - nome:
            - quantidade:
            - preço
        Produto 2:
            - nome:
            - quantidade:
            - preço
'''

carrinho = []

produto1 = {'nome': 'XBox One S', 'quantidade': 1, 'preço': 2000}
produto2 = {'nome': 'Nintendo Switch', 'quantidade': 1, 'preço': 2300}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

produto1.clear()
print(produto1)

print(produto2.values())

produto2.popitem()
print(produto2)

#=================================================================================================================
print('\n')

# Copiando dados:

# Forma 1: -> Deep Copy

d = dict(a=1, b=2, c=3)
print(d)

novo = d.copy()

print(novo)


novo['d'] = 4

print(novo)

print('\n')
# Forma 2: -> Shallow Copy

novo = d
print(novo)

novo['d'] = 4
print(novo)

print(d)
print(novo)

#=================================================================================================================
print('\n')
# Forma alternativa e não usual de criação de dicionários:

outro = {}.fromkeys('a', 'b')
print(outro)

print('\n')
dicionario = {}.fromkeys(['nome', 'idade', 'altura'], 'desconhecido')
#Transforma os valores dos elementos na lista (chaves) como 'desconhecido'
print(type(dicionario))
print(dicionario)

print('\n')

outro_2 = {}.fromkeys('chave', 'valor')
print(outro_2) #Para cada letra da palavra chave, ele criou uma chave, todas com o...
#... valor contidos a string 'valor'

print('\n')
see = {}.fromkeys(range(0, 8), 'nada')
print(see)
#Cria um dicionário em que as chaves vão de 0 a 8, todas com os valores como strings 'nada'