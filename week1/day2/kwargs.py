"""
**kwargs (podemos usar com qualquer nome, desde que tenha os dois asteriscos **)

-> Este é só mais um parâmetro, só que diferente do *args que coloca os valores extras em uma tupla, o
**kwargs exige que utilizemos parâmetros nomeados que serão colocados em dicionários
"""
print("\n")

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')
    #return kwargs

cores(Felipe='Verde', Adriano='Vermelho', Carlos='Preto')

cores()

#OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores(Pikachu='Amarelo', Charizard='Laranja')

#=================================================================================================
print("\n")

def cumprimento_f(**kwargs):
    if 'nome' in kwargs and kwargs['nome'] == 'Felipe':
        return 'Seu nome é Felipe'
    elif 'nome' in kwargs and kwargs['nome'] == 'Ribeiro':
        return 'Seu nome não é Ribeiro'
    elif 'sobrenome' in kwargs and kwargs['sobrenome'] == 'Felipe':
        return 'Seu sobrenome não é Felipe'
    elif 'sobrenome' in kwargs and kwargs['sobrenome'] == 'Ribeiro':
        return 'Seu sobrenome é Ribeiro'
    return 'Quem é você?'

print(cumprimento_f())
print(cumprimento_f(nome='Felipe'))
print(cumprimento_f(nome='Ribeiro'))
print(cumprimento_f(nome='teste'))
print(cumprimento_f(nome='alguem', sobrenome='pessoa'))
print(cumprimento_f(nome='Qualquer', sobrenome='Ribeiro'))
print(cumprimento_f(nome='qualquer', sobrenome='Felipe'))

'''Entendendo as condições dessa função:
if 'nome' in kwargs and kwargs['nome'] == 'Felipe':

lê-se como -> SE a chave 'nome' em kwargs E essa chave
['nome'] em kwargs for igual a 'Felipe'...  '''

#Nas funções podemos declarar NESSA ORDEM:

# - Parâmetros obrigatórios
# - *args
# - Parâmetros default (não obrigatórios)
# - **kwargs

#=================================================================================================
#Exemplo:

print("\n")

def funcao(idade, nome, *args, estudante=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if estudante:
        print(f'{nome} é estudante')
    else:
        print(f'{nome} não é estudante')
    print(kwargs)

print(funcao(2, 'Adriano', estudante=False))
print(funcao(18, 'Felipe', 'args aqui', True)) #Perceba que o True será considerado parte do args
#Para considerar esse argumento como parte do parâmetro estudante, deve-se fazer:...
#... estudante=True/False
#Então poderia ficar:

print(funcao(18, 'Felipe', 'args', 33, ['lista'], estudante=True))
#Perceba:                  [corresponde ao args]  [  estudante  ] 

#=================================================================================================
print("\n")

def show_info(a, b, *args, pessoa='Felipe', **kwargs):
    return [a, b, args, pessoa, kwargs]

print(show_info(1, 2, 'qualquer coisa', 'aaaa', pessoa='Outra pessoa', algo='algo para kwargs'))

#=================================================================================================
print("\n")

def mostra_cores(**kwargs):
    return kwargs['cor'] + ' ' + kwargs['tonalidade']

cores = {'cor': 'Verde', 'tonalidade': 'claro'}

#print(mostra_cores(cores())) #TypeError

print(mostra_cores(**cores))

#=================================================================================================
print("\n")

def soma_elementos(a, b, c):
    return a+b+c

lista = [1, 2, 3]
conjunto = {1, 2, 3} #conjunto = set
tupla = (1, 2, 3)

print(soma_elementos(*lista))
print(soma_elementos(*conjunto))
print(soma_elementos(*tupla))

new_lista = [1, 2, 3, 4, 5]
#print(soma_elementos(*new_lista)) #Erro de excesso de elementos

dicionario = {'a': 1, 'b': 2, 'c': 3}
print(soma_elementos(**dicionario))
#O nome das chaves nos dicionários devem ser os mesmos dos parâmetros da função

new_dicionario = {'d': 1, 'e': 2, 'f': 3}
#print(soma_elementos(**new_dicionario)) #Erro: chaves com nomes diferentes