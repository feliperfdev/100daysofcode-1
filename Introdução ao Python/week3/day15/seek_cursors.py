'''
Seek e Cursors

seek -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que
indica onde queremos colocar o cursor.

Passos para se trabalhar com um arquivo:

1 -> Abrir o arquivo
2 -> Trabalhar o arquivo
3 -> Fechar o arquivo
'''
print('\n')

arquivo = open('C:/Users/felip/OneDrive/Área de Trabalho/Github/100daysofcode/Introdução ao Python/week3/day15/texto.txt')

print(arquivo.read())

arquivo.close() # Verifica se o arquivo está aberto ou fechado

print('\n')
print(bool(arquivo.close())); print('\n')
#========================================================================================================
# Quando um arquivo é fechado e desejamos utilizá-lo novamente, é necessário chamar a abertura dele

arquivo = open('C:/Users/felip/OneDrive/Área de Trabalho/Github/100daysofcode/Introdução ao Python/week3/day15/texto.txt')

# Movimentando o cursor pelo arquivo com a função seek():

arquivo.seek(0) # Volta para a posição 0 do arquivo
print(arquivo.read()); print('\n')

# arquivo.readline() --> Lê o arquivo linha por linha
arquivo.seek(0)

print(arquivo.readline())

print('\n')
#========================================================================================================

arquivo.seek(0)

retorno = arquivo.readline()

print(retorno.split(' '))
#========================================================================================================

arquivo.seek(0) ; print('\n')

retorno2 = arquivo.read()

print(retorno2.split('\n'))

#========================================================================================================
print('\n')

arquivo.seek(0)

linhas = arquivo.readlines() # Retorna uma lista de strings
print(f'Tem {len(linhas)} linhas') # Saber quantas linhas tem no arquivo

print('\n')

arquivo.close()
#========================================================================================================

arquivo = open('C:/Users/felip/OneDrive/Área de Trabalho/Github/100daysofcode/Introdução ao Python/week3/day15/texto.txt')

# Limitando a quantidade de caracteres a serem lidos:

print(arquivo.read(21))

arquivo.close()