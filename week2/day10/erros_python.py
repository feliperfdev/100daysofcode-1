'''
Erros mais comuns em Python:

OBS: Importante ler e prestar atenção na saída de erro

NameError --> Ocorre quando uma variável ou função não foi definida

SyntaxError --> Ocorre quando é encontrado um erro de sintaxe no Python. Ou seja, foi
escrito algo que não é reconhecido como parte da linguagem Python

TypeError --> Ocorre quando uma função/operação/ação é aplicada a um tipo que não devia

IndexError --> Ocorre quando tentamos acessar um elemento ou dado indexado em um
iterável usando um índice invalido

ValueError --> Ocorre quando uma função ou operação built-in(integrada) recebe um argumento
com tipo correto, porém com valor inapropriado

KeyError --> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

AtributeError (POO) --> Ocorre quando uma variável não tem atributo ou função

IndentationError --> Ocorre quando a identação do Python não é respeitada (quatro espaços)


OBS: Exception e Error são sinônimos na programação

Mais erros: {https://docs.python.org/3/library/exceptions.html}
'''
print('\n')

'''
# SyntaxError:

--> print(Hello World)

--> def funcao(algo)
        print(algo)

--> return

--> def = 10

# NameError:

--> printf('Hello, World!')

--> a = 10
if a < 10:
    msg = ' "a" é menor que 10 '

print(msg)

# TypeError:

--> print(len(10))
--> print(len('Felipe' + []))

# IndexError:

--> lista = [1, 2, 3]
    print(lista[4])

--> nome = ['Felipe']
    print(nome[0][10])

# ValueError:

--> print(int('Felipe'))

# KeyError:

--> dictio = {'a':1, 'b':2, 'c':3, 'd':4}
    print(dictio['e'])

# AtributeError:

--> tupla = 11, 7, 33, 27, 42, 9
    tupla.sort()
    print(tupla)

# IndentationError:

--> def funcao(var):
    return var

--> for elemento in range(10):
    elemento += 1
'''