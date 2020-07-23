'''
Set Comprehension

'''
print('\n')

# Exemplos:

numeros = {num for num in range(1, 8)}
print(numeros)

print('\n'); numeros_quad = {num**2 for num in numeros}
print(numeros_quad)

#==========================================================================================================
print('\n')

# Gerando um dicionário através de um set:

numeros = {num for num in range(1, 8)}

# Set:
numeros_quad = {num**2 for num in numeros}

# Dicionário: 
numeros_quad_dict = {num: num**2 for num in numeros} # Basta criar uma chave com a variável de...
#... referência que está sendo utilizada para realizar as operações dentro do set (no caso, o 'num')
print(numeros_quad_dict)

#==========================================================================================================
print('\n')

letras = {letra for letra in 'Felipe Ribeiro'}
print(letras)

# Gera um set desordenado e sem repetição de letras. Isso é característico dos sets.