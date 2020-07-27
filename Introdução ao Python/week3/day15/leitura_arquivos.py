'''
Leitura de arquivos

-> Para abrir o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização, é passado apenas um parâmetro de entrada,
que é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWRAPPER e é com ele que
se trabalha.

OBS: A função open() pode receber vários parâmetros, porém são opicionais. O único
obrigatório é o nome do arquivo a ser lido.

-> Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir.
Caso contrário, retornará o erro FileNotFoundError
'''
print('\n')

arquivo = open('C:/Users/felip/OneDrive/Área de Trabalho/Github/100daysofcode/Introdução ao Python/week3/day15/texto.txt')
# abrindo o arquivo

print(arquivo)
print(type(arquivo)); print('\n')

print(arquivo.read()) # Lendo o conteúdo do arquivo

#print(arquivo.read())

'''
O python utiliza um recurso chamado 'cursor', que é como o cursor do mouse, 
que funciona para ler o arquivo. É como se, para ler o conteúdo, um cursor do 
mouse fosse passando pelo conteúdo e, à medida em que isso fosse acontecendo,
o python fosse mostrando o que estava sendo lido'''
'''
A segunda execução do arquivo.read() não funcionou justamente pelo motivo de
a primeira execução dessa função já ter lido todo o conteúdo. Então não tem
nada para ser lido depois.
'''


