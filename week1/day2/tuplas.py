"""
Tuplas (tuple)

-> São representadas por parênteses
-> São imutáveis, ou seja, não pode ser modificada
-> Toda operação dentro de uma tupla, gera uma nova tupla

"""

#Relembrando as listas

lista = [1, 2, 3]
lista.append(4)
print(lista)
print("\n")

#=================================================================================================================
tupla = (1, 2, 3)
print(tupla)
print(type(tupla))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

nao_e_tupla = (4)
print(type(nao_e_tupla))

tupla4 = (4, )
print(type(tupla4))

#Podemos concluir que as tuplas são definidas pelas vírgulas, não necessariamente pelos parênteses.

#=================================================================================================================
