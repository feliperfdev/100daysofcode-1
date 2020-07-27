'''
Comando With

-> Serve para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.

'with + funcao + as + nome'

'''
print('\n')

with open('C:/Users/felip/OneDrive/Área de Trabalho/Github/100daysofcode/Introdução ao Python/week3/day15/texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed) # Retorna false pq está dentro do bloco with

print(arquivo.closed) # Retorna true pois já está fora do bloco. Logo, está fechado.

#print(arquivo.read()) --> Não funciona, pois é fechado após o bloco with