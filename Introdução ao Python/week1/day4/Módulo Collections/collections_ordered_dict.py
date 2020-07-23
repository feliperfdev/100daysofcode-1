'''
Módulo Collections -> Ordered Dict

-> Garante a ordem de inserção dos elementos

-> Nos Ordered Dict´s a ordem importa


OBS: Por convenção, nos dicionários comuns a ordem NÃO importa. No entanto, isso é diferente nos
ordered dict´s, em que a ordem importa e faz diferença, sim, na análise.

'''
print('\n')

# Recapitulando dicionários:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave}, valor = {valor}')

#==========================================================================================================
print('\n')

# Ordered Dict

from collections import OrderedDict

dicionario_ = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave_, valor_ in dicionario_.items():
    print(f'chave = {chave_}, valor = {valor_}')

#==========================================================================================================
print('\n')

# Entendendo a diferença entre o Dict e o Ordered Dict:

dict1 = {'a': 1, 'b':2}
dict2 = {'b':2, 'a': 1}

print(dict1 == dict2) # Retorno booleano (True/False)   ---> True

print('\n')

dict1ord = OrderedDict({'a':1 , 'b':2})
dict2ord = OrderedDict({'b': 2, 'a':1})

print(dict1ord == dict2ord) # ---> False

# Por convenção, nos dicionários comuns a ordem NÃO importa.

# Nos Ordered Dict´s a ordem importa