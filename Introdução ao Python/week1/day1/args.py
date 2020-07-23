"""""
Entendendo o *args

-> O *args é um parâmetro como outro qualquer. Podêmos chamá-lo por qualquer nome desde que comece
com asterisco.


-> O parâmetro *args utilizado em uma função coloca os valores extras informados como entradas de uma tupla.
Lembre-se: Tuplas são imutáveis.
"""""

def soma_numeros(a=1, b=1, c=1):
    return a+b+c

print(soma_numeros(1, 2, 3))

#print(soma_numeros(1, 7)) #TypeError (caso não utilizemos parâmetros default)
print(soma_numeros(1, 7))

#print(soma_numeros(3, 5, 7, 9)) #TypeError

#======================================================================================================
print("\n")

#Entendendo o *args

def soma_todos(*args):
    print(args)

soma_todos()
soma_todos(1, 2)
soma_todos(1, 2, 3)
soma_todos(2, 3, 4, 5, 6, 7)

print("\n")
#======================================================================================================
def soma_todos_os_numeros(*args): #O *args é considerado um parâmetro não obrigatório
    return sum(args)

print(soma_todos_os_numeros())
print(soma_todos_os_numeros(1, 2, 3))
print(soma_todos_os_numeros(2, 3, 4, 5, 6))
print(soma_todos_os_numeros(1, 3, 5, 7, 9, 11, 13))
print(soma_todos_os_numeros(3))

#Perceba que não importa a quantidade de argumentos que são informados, a função é realizada com sucesso...
#... e todos os elementos são somados

#======================================================================================================
print("\n")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(soma_todos_os_numeros(numeros)) #TypeError

#Desenpacotador:

# num1, num2, num3, num4, num5, num6, num7, num8, num9 = numeros
#print(soma_todos_os_numeros(numeros)) #Funciona

'Porém, existe uma forma mais fácil com uma propriedade do *args:'

print(soma_todos_os_numeros(*numeros))

#O asterisco serve para que informemos ao python que estamos passando como argumento uma coleção de dados...
#... desta forma ele saberá que precisará, antes, desempacotar estes dados

tupla = (1, 3, 5, 7, 9)
print(soma_todos_os_numeros(*tupla))

#o *args não funciona com dicionários

#======================================================================================================
print("\n")

def informa(*args):
    if 'Felipe' in args and 'Ribeiro' in args:
        return 'Felipe Ribeiro'
    return 'What?' #else

print(informa())
print(informa(1, 2, 3, 'Felipe', False, True, []))
print(informa({}, (), 'sijdd', 'Ribeiro'))
print(informa('Felipe', 'Ribeiro', False, soma_todos_os_numeros(1, 2, 3)))
print(informa('Ribeiro', 32, 5, 7, 9, soma_todos_os_numeros(1, 3, 4)))

#Não importa quantos argumentos sejam informados, ele entra na condição e tenta verificar o que foi solicitado
#No caso, apenas o 4º print() atende à condição estabelecida na função. Entretanto, não impediu dos outros...
#... print´s serem executados, afinal, eles atenderam ao que seria a condicional 'else'