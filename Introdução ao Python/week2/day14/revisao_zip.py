print('\n')

cidade  = 'Salvador', 'São Paulo', 'Rio de Janeiro'
temperatura = 35, 29, 40

print(list(zip(cidade, temperatura)))

print('\n')

teste = {dado[0]: dado[1] for dado in zip(cidade, temperatura)}
print(teste)

#========================================================================================================
print('\n')


prog = 'Python', 'Java', 'C++', 'Lua', 'Javascript', 'R', 'C#'

rank = 1, 3, 7, 5, 2, 6, 4

organiza = {dado[0]: dado[1] for dado in zip(rank, prog)}
# cria o dicionário contendo chave e valor de cada elemento do zip

print(organiza); print('\n')

print(sorted(organiza.items(), key=lambda valor: valor))
# Organiza por ordem numérica

'''
O que aconteceu na variável 'organiza'?

-> Foi 'criada' uma variável auxiliar (dado), que foi utilizada para
ser chave acessando o índice 0 do zip e para ser valor acessando o
índice 1 do zip. 

-> Lembrar que o zip cria uma LISTA contendo tuplas, sendo que cada tupla
contém como elementos os valores dos iteráveis passados para o zip.
Dentro de cada tupla são armazenados valores de um por um de cada iterável.
Ou seja, nas tuplas sempre terão valores de iteráveis diferentes, nunca dos
mesmos iteráveis dentro de uma única tupla.

-> Como queria passar para dicionário, foi pedido para o dado no índice 0
ser a chave e o dado no índice 1 ser o valor para cada dado contido no zip()

'''