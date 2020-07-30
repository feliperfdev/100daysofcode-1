'''
Forçando tipos de dados com Decoradores

'''
print('\n')

'''
Relembrando o zip:

a = (1, 2, 3)
b = (4, 5, 6)

c = zip(a, b)
print(c) ===> (1, 4), (2, 5), (3, 6)
'''

# Definindo uma função:

def forca_tipo(*tipo):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipos) in zip(args, tipo):
                novo_args.append(tipos(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Python', 4)

print('\n')
#======================================================================================================

for vezes in range(4):
    print('Python')

print('\n')
#======================================================================================================

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir(4, 2)
dividir(9, 7)
dividir(27, 9)