'''
Dictionary Comprehension

# Sintaxe:

{chave: valor for valor in iterável}

'''
print('\n')

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

numeros_quadrado = {chave: valor**2 for chave, valor in numeros.items()}
print(numeros_quadrado)

#==========================================================================================================
print('\n')

num = [1, 2, 3, 4, 5, 6, 7]

num_quad = {valor: valor**2 for valor in num}
print(num_quad)
# Ele pega cada valor da lista e transforma na chave, depois pega esses mesmos valores, eleva ao...
# ... quadrado e transforma nos valores

num1 = [1, 1, 2, 3, 3, 4]
num1_quad = {valor1: valor1**2 for valor1 in num1}
print(num1_quad)

# Como o dicionário, por convenção, não pode repetir as chaves, quando temos uma lista com valores...
# ... repetidos, ao serem transformados para o dicionário os valores repetidos são ignorados.

#==========================================================================================================
print('\n')

chave = 'abcde'
valores = [1, 2, 3, 4 ,5]

mistura = {chave[i]: valores[i] for i in range(0, len(chave))}
print(mistura)

#==========================================================================================================
print('\n')

numbers = [1, 2, 3, 4, 5]
par_impar = {nums:('par' if nums%2==0 else 'impar') for nums in numbers}

print(par_impar)