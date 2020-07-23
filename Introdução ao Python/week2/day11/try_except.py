'''
Bloco Try / Except

-> Utilizamos o bloco Try / Except para tratar erros que podem ocorrer no nosso código.
Previnindo, assim, que o programa pare de funcionar e o usuário receba mensagem de erro
inesperada.


try:
    //execução do problema

except:
    //o que deve ser feito em caso de problema

'''
print('\n')

# Exemplo 1:

try:
    funcao()

except:
    print('Não foi possível executar')

# Exemplo 2:    Tratando um erro genérico

try:
    len(5)

except:
    print('Algo deu errado')

# Exemplo 3:    Tratando um erro específico

try:
    nova_funcao()

except NameError:
    print('Essa função não existe')

try:
    len(33)

except TypeError:
    print('Você está utilizando um tipo errado nessa função')

# Exemplo 4:    Detalhes para o erro

try:
    len(42)

except TypeError as error:
    print(f'A aplicação gerou o seguinte erro: {error}')

# Exemplo 5:    Efetuando diversos tratamentos de erro de uma vez

try:
    len(57)

except NameError as error:
    print(f'Deu NameError: {error}')
except TypeError as error:
    print(f'Deu TypeError: {error}')
except ValueError as error:
    print(f'Deu ValueError: {error}')

# Exemplo 6:

try:
    print('Felipe'[11])
except IndexError as error:
    print(f'Deu um erro de índice: {error}')

# Exemplo 7:

def mostraValor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as error:
        return f'Essa chave não existe: {error}'
    except TypeError as error:
        return f'Tipo de chave não permitido: {error}'

dicionario = {'idade': 18}

print(mostraValor(dicionario, 'idade'))

print(mostraValor(dicionario, 'nome'))
print(mostraValor(dicionario, dicionario))

#========================================================================================================

# Exemplo extra:

try:
    len(33)
except TypeError as error:
    print(f'Argumento informado do tipo errado: {error.__class__}')