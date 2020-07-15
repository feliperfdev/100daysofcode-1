""""
Dictionaries (dict)

-> Em outras linguagens os dicionários podem ser chamados de 'mapas'

-> Dicionários são coleções do tipo chave/valor --> {chave:valor}
-> São representados por chaves {}
-> Tanto chaves quanto os valores podem ser de quaisquer tipos de dados
-> Dicionários não são indexados

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