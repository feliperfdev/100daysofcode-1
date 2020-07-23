'''
Levantando os próprios erros com Raise

*OBS: Não é uma função, e sim uma palavra revervada (como o def)

raise -> lança exceções

É útil para criarmos nossas próprias exceções e mensagens de erro

Como usar:

raise TipoDoErro('mensagem de erro')


OBS: O raise, assim como o return, finaliza o bloco de função. Ou seja, nada pode ser executado
após a execução do raise
'''

#raise ValueError('Valor incorreto')

print('\n')

# Exemplos:

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'vermelho', 'azul')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if cor not in cores:
        raise ValueError('Cor não permitida')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    return f'O texto {texto} é da cor {cor}'


print(colore('Felipe', 'verde'))
print(colore('Cesar', 'vermelho'))
print(colore('Camila', 'cinza')) # ValueError: Cor não permitida

#print(colore('Felipe', 6)) # TypeError: Cor precisa ser uma string

print(colore(4, 'azul')) # TypeError: Texto precisa ser uma string