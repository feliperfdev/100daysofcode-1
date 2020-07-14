"""""
Funções com Parâmetro Padrão (Default Parameters)

- São funções onde a passagem de parâmetro seja opcional;

- Podemos declarar QUALQUER tipo de dado para parâmetros padrões
Podendo ser: números, strings, floats, booleanos, listas,
dicionários, tuplas, funções...
"""""

print('Hello, world!')
print() #mesmo sem parâmetro, o print não dá erro

#==========================================================================
print("\n")

def quadrado(numero): #Exemplo de função onde a passagem de...
    #...parâmetro seja obrigatória
    return numero**2

print(quadrado(2))
# print(quadrado()) -> não pode

#==========================================================================
print("\n")

def exponencial(numero, potencia=2):
    return numero**potencia

'Quando um parâmetro numa função recebe um valor, a definição' \
'dele se torna opcional. Ou seja, caso não o declaremos, será' \
'executado o seu padrão (definido na passagem de parâmetros)' \
'No caso dessa função, caso não informemos o argumento na chamada' \
'da função, por padrão ele será 2. Entretanto podemos informar' \
'outro argumento caso quisessemos que fosse outro valor.'

print(exponencial(2, 3)) # 2x2x2
print(exponencial(3, 2)) # 3x3

print("\n")
print(exponencial(4)) #por padrão, eleva ao quadrado
print(exponencial(3, 4)) # eleva à potência informada

#==========================================================================
print("\n")

#Erro
'''def teste_erro(num=2, potencia):
    return num ** potencia

print(teste_erro(4))'''

#Maneira correta
def teste_correto(potencia, num=2):
    return num ** potencia

print(teste_correto(5))

'Para declarar um parâmetro default numa função com mais de' \
'um parâmetro ele nunca deve ficar como primeiro na passagem ' \
'de parâmetros. O correto é sempre deixar ele na segunda posição' \
'para frente.'

#==========================================================================
print("\n")

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
#print(soma(4)) #TypeError
#print(soma()) # Type Error

def nova_soma(num1, num2=0):
    return num1 + num2

print(nova_soma(9, 3))
print(nova_soma(4))
#print(nova_soma()) #TypeError

#==========================================================================
print("\n")

def mostra_nome(nome='', sobrenome=''):
    if nome == 'Felipe' and sobrenome == 'Ribeiro':
        return 'Você é Felipe Ribeiro!'
    elif nome == 'João' and sobrenome == 'Pedro':
        return 'Você é João Pedro!'
    else:
        return 'Quem é você?'

print(mostra_nome())
'não deu erro pq na função eu declarei os parâmetros como se' \
'recebessem strings vazias, tornando a declaração delas' \
'opcionais como argumentos'

print(mostra_nome('Felipe', 'Ribeiro'))
print(mostra_nome('João', 'Pedro'))
print(mostra_nome('Qualquer', 'Pessoa'))

#==========================================================================
print("\n")

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def mat(a, b, fun=soma):
    return fun(a, b)

print(mat(1, 2)) #por padrão, serão somados
print(mat(5, 7, subtrai))
print(mat(8, 9, soma))

#==========================================================================
print("\n")

#Variáveis globais e Variáveis Locais

pessoa = 'Felipe' #Variável global

def diz_oi():
    return f'Oi, {pessoa}'

print(diz_oi())

def diz_oi_2():
    pessoa = 'Anybody'
    return f'Oi, {pessoa}'

print(diz_oi_2())

'Dentro de um escopo de função, se tivermos uma variável local' \
'com o mesmo nome de uma variável global, a local será priorizada'


def alguem():
    humano = 'Existe'
    return humano

print(alguem())
#print(humano) #TypeError
'Variáveis locais não podem ser executadas no escopo global'

'ATÊNÇÃO! Sempre que puder evitar variáveis globais, evite!'

#==========================================================================
print("\n")

total = 0
def incrementa():
    global total #Isso é um aviso dizendo que quero utilizar...
    #... a variável global
    total += 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa()) #Vai incrementando à medida que a função...
#... é chamada

#==========================================================================
print("\n")

def fora():
    cont = 0
    def dentro():
        nonlocal cont
        cont += 1
        return cont
    return dentro()

#print(dentro()) #NameError
print(fora())
print(fora())
print(fora())