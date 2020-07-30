'''
Decoradores -> Decorators

--> São funções
--> Envolvem outras funções e aprimoram seus comportamentos
--> São exemplos de High Order Functions
--> Possuem sintaxe prórpia. Utilizam o '@'. (Syntax Sugar)

'''
print('\n')

def cumprimento(funcao):
    def morning():
        print('Bom dia!')
        funcao()
        print('Tenha um ótimo dia!')
    return morning

def hello():
    print('Seja bem vindo(a)!')


teste = cumprimento(hello)

print(teste());                                                     print('\n')

def raiva():
    print('Estou bravo!')

cumprimento_raiva = cumprimento(raiva)

print(cumprimento_raiva());                                     print('\n')

#======================================================================================================

# Decorators com Syntax Sugar

def cumprimentoNovo(funcao):
    def morning():
        print('Bom dia!')
        funcao()
        print('Tenha um excelente dia!')
    return morning

@cumprimentoNovo    # Decorator
def pergunta():
    print('Tudo bem?')

print(pergunta());                                                                  print('\n')


@cumprimentoNovo
def dormir():
    print('Estou com sono!')

print(dormir())

print('\n')
#======================================================================================================

# Exemplo de utilização de decorator:

# Suponha que tenha um site

'''
https://www.suaempresa.com.br

Abas:

[Home] [Produtos] [Serviços] [Administrativo]

https://www.suaempresa.com.br/home
https://www.suaempresa.com.br/produtos
https://www.suaempresa.com.br/serviços
https://www.suaempresa.com.br/admin ---> Só pode acessar se for usuário do site

def checa_login():
    if not request.usuario:
        request('https://www.suaempresa.com.br')

def home(request):
    return 'Acesso a Home permitido'

def produtos(request):
    return 'Acesso a Produtos permitido'

def serviços(request):
    return 'Acesso a Serviços permitido'

@checa_login
def admin(request):
    return 'Acesso a Administrativo permitido
'''

#======================================================================================================

# OBS: Não confundir decorator com decoration function
