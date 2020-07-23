'''
List Comprehension 1

-> Utilizando List Comprehension, nós podemos gerar novas listas com dados processados a partir
de outro iterável

'''

# Sintaxe:
 
'''
[dado for dado in iterável]
'''

# Exemplos:

print('\n')

lista = [1, 2, 3, 4, 5]

res = [numero*10 for numero in lista]
print(res)        #Lê-se: Para cada número na lista, pegue esse número e multiplique por 10

#==========================================================================================================
print('\n')

def quadrado(valor):
    return valor*valor

res = [quadrado(number) for number in lista]
print(res)

#==========================================================================================================
print('\n')

numeros = [1, 2, 3, 4, 5, 6]
numero_dobro = []

# Utilizando loop:

for numero in numeros:
    numero_dobrado = numero*2
    numero_dobro.append(numero_dobrado)

print(numero_dobro)

# Utilizando List Comprehension:

numeros = [1, 2, 3, 4, 5, 6]
print('\n'); print(numero*2 for numero in numeros) # ou print(numero*2 for numero in [1, 2, 3, 4, 5, 6]) 

#==========================================================================================================
print('\n')

# Ex1:

nome = 'felipe'

print([letra.upper() for letra in nome]) # Gera uma lista com cada letra da string em caixa alta

# Ex2:

def caixa_alta_letra(palavra):
    palavra = palavra.replace(palavra[0], palavra[0].upper())
    return palavra

nomes = ['felipe', 'joão', 'júlia', 'césar', 'marcos', 'camila']

print([caixa_alta_letra(letra) for letra in nomes])

# Ex3:

print('\n')

print([num*3 for num in range(0, 11)])

# Ex4:

print('\n')

print([bool(valor) for valor in [1, 2, [], 4, True, 5, 6, 7]])

# Ex5:

print('\n')

print([str(numero_) for numero_ in [1, 2, 3, 4, 5]])