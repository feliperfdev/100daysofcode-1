'''
Len / Abs / Sum / Round

len() -> Retorna o tamanho de um iterável(quantidade de items dentro) ou de um dado
abs() -> Retorna o valor absoluto (módulo) de um número inteiro ou real
sum() -> Retorna a soma de todos os valores de um iterável
round() -> Retorna o valor aproximado de número com 'n' precisão. Se a precisão não for informada...
...será retornado o inteiro mais próximo de entrada
'''
print('\n')

# >>>>>>>>> len() <<<<<<<<<

print(len([1, 2, 3, 4, 5, 6])) # 6
print(len({1, 2, 3, 4, 5, 6}))
print(len((1, 2, 3, 4, 5, 6)))
print(len('Felipe Ribeiro')) # 14 (o espaço vazio entre as strings conta)

# O que acontece quando se utiliza o len()?

print('String qualquer'.__len__()) 

# OBS: Toda função em python que começa e termina com dois underlines (__), é chamada de 'Dunder'

print('\n')
#========================================================================================================

# >>>>>>>>> abs() <<<<<<<<<

print(abs(-33))
print(abs(-0.56))

# Utilizando Generator Expression:
negativos = [-1, -2, -3, -4]
gen_neg = (abs(num) for num in negativos)
print(list(gen_neg))

print('\n')

#========================================================================================================

# >>>>>>>>> sum() <<<<<<<<<

# O sum() além de somar todos os valores de um iterável, ainda recebe um segundo argumento (chamado de...
#... valor inicial)

print(sum([1, 2, 3, 4], 5))

# Em que situação poderiamos utilizar o valor inicial?

# Suponha que em uma loja online você compra alguns produtos:
# E nessa loja possui um frete FIXO que é aplicado ao valor final de todos os produtos do carrinho

valores = [3000, 4000, 500]

print(sum(valores, 50)) # Supondo frete de R$50.00

print('\n')

#========================================================================================================

# >>>>>>>>> round() <<<<<<<<<

# ---> round(número, precisão)

print(round(10.2)) # 10
print(round(10.6)) # 11

print(round(2.7182818284590452353602874)) # Retorna o inteiro mais próximo
print(round(2.7182818284590452353602874, 2))
print(round(2.7182818284590452353602874, 4))
print(round(2.7182818284590452353602874, 7));               print('\n')

print(round(3.14159265359)) # Retorna o inteiro mais próximo
print(round(3.14159265359, 2))
print(round(3.14159265359, 5));                             print('\n')

from math import pi

print(round(pi, 1))
print(round(pi, 2))
print(round(pi, 8))