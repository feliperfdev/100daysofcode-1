'''
Any & All

--> all() -> retorna True e todos os elementos do iterável são verdadeiros ou se o iterável está vazio

'''
print('\n')

# Relembrando: Quando o número 0 (zero) é analisado em booleano, será retornado False

# >>>>>>>>>> Exemplo all(): <<<<<<<<<

print(all([1, 2, 3, 4, 5, 6])) # ---> True
print(all([0, 1, 2, 3])) # ---> False (pois o 0 (zero) está na lista)
print(all([])) # ---> True // Iterável vazio
print(all((1, 2, 3, 4))) # ---> True
print(all({})) # ---> True // Iterável zazio
print(all({1, 2, 3, 5})) # ---> True
print(all({1, 2, 0, 3, 5})) # ---> False // Zero (0) aparece

print('\n')
#=========================================================================================================

nomes = ['Carlos', 'Cleber', 'Claudia', 'Cesar', 'Camlila']

print(all([nome[0]=='C' for nome in nomes])) # ---> True
print(all([nome[0]=='A' for nome in nomes])); print('\n') # ---> False

#=========================================================================================================

print([letra for letra in 'eio' if letra in 'aeiou']) # retorna ['e', 'i', 'o']
print([letra for letra in 'eFio' if letra in 'aeiou']) # retorna ['e', 'i', 'o']

print(all([letra for letra in 'eio' if letra in 'aeiou'])) # ---> True
print(all([letra for letra in 'eFio' if letra in 'aeiou'])); print('\n') # ---> True

print([letra for letra in 'afk' if letra in 'eiou']) # retorna []
print(all([letra for letra in 'afk' if letra in 'eiou'])) # ---> True
# OBS: Como é retornado um iterável vazio ([]), o all() continua retornando True

print('\n')
#=========================================================================================================

# Análise dos números na lista // Convertendo para booleano os números pares da lista
print(all([numero for numero in [2, 4, 6, 8, 10] if numero%2==0])) # ---> True

print(all([numero for numero in [2, 4, 0, 8, 10] if numero%2==0])) # ---> False (por causa do 0 (zero))

#=========================================================================================================

# >>>>>>>>>> Exemplo any(): <<<<<<<<<

'''
--> Retorna True se QUALQUER elemento do iterável for verdadeiro
--> Retorna False se o iterável estiver vazio
'''

print(any([1, 2, 3, 4, 5])) # --> True
print(any([1, 2, 0, 3, 4, 5])) # --> True // Mesmo que tenha um elemento False, todos os outros são True
print(any([0, 0, 0, 0])) # --> False // Pois todos os elementos são False
print(any([0, 0, 0, 1])) # --> Ture // Basta um elemento verdadeiro para tornar True

print(any([0, [], {}, (), False])); print('\n') # --> False // Todos são elementos False

#=========================================================================================================

nomes = ['Carlos', 'Cleber', 'Claudia', 'Cesar', 'Camlila', 'Felipe']

print(any([nome[0]=='C' for nome in nomes])) # --> True
# Por mais que tenha um nome que comece com letra diferente de 'C', ainda existem elementos com 'C'...
#... dentro desse iterável, validando o True

outros_nomes = ['Carlos', 'Marco', 'Vanessa', 'Ana', 'Felipe']

print(any([nome[0]=='Z' for nome in outros_nomes])) # --> False // Nenhum nome nesse iterável...
#... começa com 'Z'

print(any([nome[0]=='F' for nome in outros_nomes])) # --> True

print(any([num for num in [4, 2, 3, 10, 8, 6, 9, 11, 12] if num%2==0])) # --> True
# Por mais que tenhamos elementos ímpares na lista, existem elementos pares, o que já é suficiente...
#... para validar o True

print(any([num for num in [1, 3, 5, 7] if num%2==0])) # --> False
print(any([num for num in [1, 3, 5, 7, 8] if num%2==0])) # --> True // Perceba que apenas um...
#... elemento True já é o suficiente para a validação