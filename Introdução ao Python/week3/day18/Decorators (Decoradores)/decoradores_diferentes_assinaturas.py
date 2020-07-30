'''
Decoradores com Diferentes Assinaturas

# Para resolver, utilizamos Decorator Patterns

--> O nome, parâmetro e retorno são as assinaturas de uma função
'''
print('\n')

# Relembrando decoradores:

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def pessoa(nome):
    return f'Olá {nome}'

print(pessoa('Felipe'))

print('\n')
#======================================================================================================

'''
@gritar
def pedido(principal, acompanhamento):
    return f'Gostaria de um(a) {principal} acompanhado de {acompanhamento}'

# Nesse caso terá erro, pois a função aumentar() recebe apenas um parâmetro.
'''

# Deve-se utilizar Decorator Pattern para soluciona

# Refatorando:

def gritarRefatorada(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritarRefatorada
def pedido(principal, acompanhamento):
    return f'Gostaria de um(a) {principal} acompanhado(a) de {acompanhamento}'

print(pedido('Picanha', 'Batata Frita'))

print('\n')

@gritarRefatorada
def risada():
    return 'kkkkkkkkkkkkkk'

print(risada())

print('\n')
#======================================================================================================

# Lembre-se que com **kwargs podemos nomear os parâmetros

print(pedido(principal='Pizza', acompanhamento='Brownie'))
print(pedido(acompanhamento='Pastel', principal='Pizza'));                              print('\n')

#======================================================================================================

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Precisa ser: {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento(10)
def soma_com_dez(a, b):
    return a+b

print(soma_com_dez(10, 12))
print(soma_com_dez(1, 33));                                                                 print('\n')

@verifica_primeiro_argumento('calabresa')
def pizza(sabor1, sabor2):
    return f'Pizza sabor {sabor1} e {sabor2}'

print(pizza('calabresa', 'frango'))
print(pizza('brigadeiro', 'calabresa'))
print(pizza('4 queijos', 'doce'))