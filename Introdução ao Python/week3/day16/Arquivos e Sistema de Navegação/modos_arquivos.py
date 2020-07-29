'''
Modos de abertura de arquivos

Documentação: {https://docs.python.org/3/library/functions.html#open}

'r' -> abre para leitura (padrão/default)
'w' -> abre para escrita (sobrescreve caso o arquivo já exista)
'x' -> abre para escrita somente se o arquivo não existir
'a' -> abre para escrita e adiciona ao arquivo caso ele exista
'b' -> modo binário
't' -> modo de texto (default)
'+' -> abre para atualização (leitura e escrita)

'''
print('\n')

with open('new_file.txt', 'a+') as arquivo:
    arquivo.write('Teste\n')
    arquivo.write('Outro teste\n')

# se usar 'x'  --> retorna FileExistsError
# se usar 'a' --> realiza a função write() novamente // adiciona o conteúdo ao arquivo sem prejudicar o...
#... conteúdo já existente

#formas de usar o '+' --> 'w+' 'a+' 'r+'