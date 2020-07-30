'''
Preservando Metadata com Wraps

Metadatas (metadados) -> São dados intrísecos em arquivos.
Wraps -> São funções que envolvem elementos com diversas finalidades.

'''
print('\n')

def ver_log(funcao):
    def logar(*args, **kwargs):
        "Função dentro de uma função"
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Documentação da função: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def somar(a, b):
    "Função que realiza soma"
    return a + b

print(somar(1, 7));                                                                           print('\n')


print(somar.__name__) # logar
print(somar.__doc__) # documentação de logar
# Metadata está incorreta.

'''
OBS: O erro de Metadata não retorna um erro. O que acontece é que, nesse caso, ao utilizar o
__name__ e o __doc__, foram informados o nome e a documentação da função 'logar()', não da
função 'somar()'.
'''

print('\n')
#======================================================================================================

# Resolvendo esse problema

from functools import wraps # Fazer import do 'wraps' da biblioteca 'functools'

def ver_log(funcao):
    @wraps(funcao) # Utilizar o wraps como decorator
    def logar(*args, **kwargs):
        "Função dentro de uma função"
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Documentação da função: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def somar(a, b):
    "Função que realiza soma"
    return a + b

print(somar(1, 7));                                                                 print('\n')

# O @wraps solucionou o erro de metadata
print(somar.__name__) # somar
print(somar.__doc__) # Documentação de somar --> ("Função que realiza soma")


#======================================================================================================
#======================================================================================================
#======================================================================================================
print('\n')

def calcula(function):
    def doc_funcao(*args, **kwargs):
        "Mostra nome e documentação da função"
        print(f'Documentação: {function.__doc__}')
        print(f'Nome: {function.__name__}')
        return function(*args, **kwargs)
    return doc_funcao

@calcula
def multiplica(a, b):
    "Função que realiza multiplicação"
    return a * b

print(multiplica(3, 4));                                                            print('\n')

# Erro de metadata
print(multiplica.__name__)
print(multiplica.__doc__)

print('\n')
#======================================================================================================

# Resolvendo o erro:

def calcula(function):
    @wraps(function) # chamando o wraps como decorator
    def doc_funcao(*args, **kwargs):
        "Mostra nome e documentação da função"
        print(f'Documentação: {function.__doc__}')
        print(f'Nome: {function.__name__}')
        return function(*args, **kwargs)
    return doc_funcao

@calcula
def multiplica(a, b):
    "Função que realiza multiplicação"
    return a * b

print(multiplica(3, 4));                                                            print('\n')

# Erro de metadata
print(multiplica.__name__)
print(multiplica.__doc__)