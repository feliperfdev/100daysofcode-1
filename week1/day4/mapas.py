"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

"""
print('\n')

receita = {'jan': 100, 'fev': 150, 'mar': 200}

#Iterando com dicionários

for chave in receita:
    print(chave)

print('\n')
for chave in receita:
    print(receita[chave])

print('\n')
for chave in receita:
    print(f'{chave} : {receita[chave]}')

#=================================================================================================================
print('\n')
print(receita.keys()) # Retorna um dicionário de chaves

for chave in receita.keys():  # Recomendado fazer desta maneira  --> Informar que está acessando as chaves
    print(receita[chave])


print('\n')
print(receita.values()) # Retorna um dicionário de valores

for valor in receita.values(): # Recomendado fazer desta maneira  --> Informar que está acessando os valores
    print(valor)

#=================================================================================================================
print('\n')

print(receita.items())

for chave_, valor_ in receita.items():
    print(f'Chave: {chave_}, Valor: {valor_}')
#=================================================================================================================
print('\n')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))