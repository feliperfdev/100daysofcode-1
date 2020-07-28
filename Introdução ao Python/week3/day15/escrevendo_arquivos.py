'''
Escrevendo em arquivos


OBS: Ao abrir um arquivo para LEITURA, não podemos realizar escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para ESCRITA, não podemos lê-lo (no terminal), apenas escrever.

Quando é criado um arquivo para escrita, ele é criado no sistema operacional com o nome escolhido
e com o que foi feito/escrito nele.

-> Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir, será criado. Caso já exista,
o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo do arquivo anterior é perdido.

'''
print('\n')

with open('novo_arquivo.txt', 'w') as arquivo: # o 'w' vem de 'write'
    arquivo.write('Posso escrever qualquer coisa aqui.')
    arquivo.write('\nIsso é apenas um teste')
    arquivo.write('\nÚltima linha desse teste')

# --> Função write() serve para escrever e recebe APENAS strings