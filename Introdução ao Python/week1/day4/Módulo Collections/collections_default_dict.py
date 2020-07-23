'''
Collections - Default Dict

Ao criar um dicionário utilizando o Dafault Dict, nós informamos um valor default, podendo utilizar
um lambda para isso. Esse valor sempre será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave inexistente, essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores

'''
print('\n')

# Recapitulando dicionários

dicionario = {'nome': 'Felipe', 'sobrenome': 'Ribeiro'}

print(dicionario)
print(dicionario['nome'])
#print(dicionario['nao_existe']) --> KeyError

#==========================================================================================================
print('\n')

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['nome_meio'] = 'Azevedo'
print(dicionario['nao_existe']) # Retorna o valor do lambda e cria a chave 'nao_existe' com esse valor
print(dicionario) # Resultado é refletido aqui