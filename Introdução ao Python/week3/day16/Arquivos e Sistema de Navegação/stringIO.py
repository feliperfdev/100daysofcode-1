'''
StringIO

Para ler um arquivo do sistema operacional, o software precisa ter permição:
    Permição de escrita -> Para escrever no arquivo
    Permição de leitura -> Para ler o arquivo

StringIO -> Utilizado para ler e criar arquivos na memória

'''
print('\n')

from io import StringIO

mensagem = 'Apenas uma string'

# Criando um arquivo em memória já com uma string ou vazio para adicionar texto depois

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write('\noutro teste')
arquivo.seek(len(mensagem))
print(arquivo.read())