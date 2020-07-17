'''
Collections - Named Tuple

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também
parâmetros


'''
print('\n')
# Recapitulando Tuplas:

tupla = (1, 2, 3)
tupla_w = 1, 2, 3, 4, 5

print(type(tupla))
print(type(tupla_w))

#==========================================================================================================
print('\n')

from collections import namedtuple

# Precisamos definir o nome e os parâmetros

# Forma 1:

cachorro = namedtuple('cachorro', 'idade raça nome') # ou: namedtuple('cachorro', 'idade, raça, nome')

# Forma 2:    ---> Utilizar dessa forma!

gato = namedtuple('gato', ['nome', 'idade'])


# USANDO:

rex = cachorro(idade=6, raça='pitbull', nome='Rex')
andy = gato(nome='Andy', idade=4)

print(rex)
print(andy)

print(f'\nIdade do gato: {andy[1]}')
print(f'Nome do cachorro: {rex[0]}')
                                        # Preferir utilizar dessa maneira abaixo:
print(f'\nNome do gato: {andy.nome}')
print(f'Raça do cachorro: {rex.raça}')

print('\n'); print(rex.index('pitbull')) # Localizar o índice
print(andy.count('Andy')) # Contar a quantidade de ocorrências