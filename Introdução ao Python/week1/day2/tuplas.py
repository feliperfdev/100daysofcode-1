"""
Tuplas (tuple)

-> São representadas por parênteses
-> São imutáveis, ou seja, não pode ser modificada
-> Toda operação dentro de uma tupla, gera uma nova tupla
-> Assim como as listas, aceitam quaisquer tipos de dados, misturados ou não.

# Operações de adição ou remoção de elementos da tupla são impossíveis. 
Considerando que as tuplas são imutáveis.

-> Sempre utilizamos tuplas quando não precisamos alterar os dados contidos nelas.

-> A imutabilidade das tuplas deixa o código mais seguro
"""
# >>>>>>>>>> DIA 2 <<<<<<<<<<

#Relembrando as listas

lista = [1, 2, 3]
lista.append(4)
print(lista)
print("\n")

#=================================================================================================================
tupla = (1, 2, 3) # -> é tupla
print(tupla) 
print(type(tupla))

tupla2 = 1, 2, 3, 4, 5 # ->  é tupla
print(tupla2)
print(type(tupla2))

nao_e_tupla = (4) # -> não é tupla // é apenas um inteiro
print(type(nao_e_tupla))

tupla4 = (4, ) # -> é tupla
print(type(tupla4))

tupla_1 = 6, # -> é tupla
print(type(tupla_1))

#Podemos concluir que as tuplas são definidas pelas vírgulas, não necessariamente pelos parênteses.

#=================================================================================================================
# >>>>>>>>>> DIA 3 <<<<<<<<<<

print("\n")
#Tuplas também podem ser geradas com a função range()

tupla_range = tuple(range(0, 11))
print(tupla_range)
print(type(tupla_range))

tupla_range2 = tuple(range(0, 20, 2))
print(tupla_range2)
print(type(tupla_range2))
#=================================================================================================================
print("\n")

tupla_str_int = 'string qualquer', 123, ['lista', 118, ['string na lista']], ('tupla', 23)
print(type(tupla_str_int))
#=================================================================================================================
print("\n")

#Desempacotamento de tuplas:

desempac_tupla = 123, 'string', ['lista', 99]
print(type(desempac_tupla))

num_tupla, str_tupla, lista_tupla = desempac_tupla

print(num_tupla)
print(str_tupla)
print(lista_tupla)
#=================================================================================================================
print("\n")

tupla_seq = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(max(tupla_seq)) #elemento máximo
print(min(tupla_seq)) #elemento mínimo
print(len(tupla_seq)) #tamanho da tupla
print(sum(tupla_seq)) #soma dos elementos da tupla
#=================================================================================================================
print("\n")

#Concatenação de tuplas

tupla1 = 1, 2, 3
tupla_2 = 4, 5, 6

#As tuplas utilizadas na operação não serão alteradas
print(tupla1)
print(tupla_2)

tupla_soma = (tupla1 + tupla_2)
print(tupla_soma) #Vai gerar uma nova tupla
#Os elementos não são somados matematicamente

print("\n")
#Tuplas são imutáveis, mas podemos SOBRESCREVER seus valores. Exemplos:

tupla3 = 9, 8, 7, 6
tupla1 = tupla1 + tupla3
print(tupla1)
print(type(tupla1))
#=================================================================================================================
print("\n")

#Interagindo com tuplas:

for e in tupla1:
    print(e, end=' ')

print("\n")
for indice, elemento in enumerate(tupla1):
    print(f'Índice: {indice} -> Elemento: {elemento}')

print("\n")
new_tupla = 'palavra', 123, ['list', 8], {'A': 'dicionário', 'B': 33}
for index, element in enumerate(new_tupla):
    print(f'Índice: {index} -> Elemento: {element}')


print("\n")
tupla_charac = 'a', 'b', 'c', 'a', 'a', 'd', 'b'
print(tupla_charac.count('a'))
print(tupla_charac.count('b'))

print(tupla_charac.index('a')) #Localizar índice do elementos 'a'
print(tupla_charac.index('a', 1)) #Localizar índices dos elementos 'a' contando a partir do índice 1
print(tupla_charac.index('b'))
print(tupla_charac.index('b', 3))

#=================================================================================================================
print("\n")
# -> Sempre utilizamos tuplas quando não precisamos alterar os dados contidos nelas. Exemplo:

tupla_meses = ('Janeiro', 'Fevereito', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                                                'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#Sabemos que existem apenas 12 meses, isso não muda. Portanto não há a necessidade de modificar algo.

print(tupla_meses)
print(type(tupla_meses))

print("\n")
print(tupla_meses.index('Março'))
print(tupla_meses.index('Maio'))

print("\n")
#Iterando com while:

i = 0
while i < len(tupla_meses):
    print(tupla_meses[i], end=' ')
    i += 1

print(f'\n{i} meses')

#=================================================================================================================
print("\n")

# Slicing de tuplas -> (início:fim:passo:)
print(tupla_meses[2:5])
print(tupla_meses[0:12:2])
print(tupla_meses[7::])

#=================================================================================================================
print("\n")

outra_tupla = 1, 2, 3
print(outra_tupla)

nova = outra_tupla #Em tuplas não existe o Shallow Copy

print(outra_tupla)
print(nova)