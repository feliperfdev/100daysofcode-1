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
#Tipo None -> 'tipo sem tipo' ou 'tipo vazio'

sem_tipo = None #Utilizamos quando queremos criar uma variável e inicializá-la com um tipo sem tipo antes...
#... de recebermos um valor final

#Ou seja, posteriormente essa variável pode receber qualquer tipo de dado.

print(sem_tipo)
print(type(sem_tipo))