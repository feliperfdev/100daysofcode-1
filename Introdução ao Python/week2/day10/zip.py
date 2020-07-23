'''
Zip


zip() --> Cria um iterável chamado 'zip object' que agrega elementos de cada um dos iteráveis passados 
como entrada em pares
'''
print('\n')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1));                                          print('\n')

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# OBS: O zip() utiliza como argumento o menor parâmetro em iterável. Ou seja, quando estivermos...
#... trabalhando com iteráveis de tamanhos diferentes, ele irá parar quando os elementos do...
#... menor iterável acabararem

print('\n')
#========================================================================================================

letras = ['a', 'b', 'c']
num = [1, 2, 3]
zip_letras_num = zip(letras, num)

print(dict(zip_letras_num));                    print('\n')

#========================================================================================================

lista_1 = [1, 2, 3, 4]
tupla = 5, 6, 7, 8
dicionario = {'a':9, 'b':10, 'c':11, 'd':12, 'e':13, 'f':14}

zip_total = zip(lista_1, tupla, dicionario.values())
print(list(zip_total));                                     print('\n')

#========================================================================================================

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados))) # Lembre-se que utilizando o asterisco(*) antes pode-se realizar o... 
#... desempacotamento dos valores dentro do iterável

print('\n')
#========================================================================================================

prova1 = [40, 67, 92, 98]
prova2 = [70, 60, 89, 90]

alunos = ['Carla', 'Rafael', 'Felipe', 'Camila']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map() para fazer o mesmo:

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

#========================================================================================================