'''
Tratando erros com Try, Except, Else e Finally

Dica de onde e quando tratar erros no código:

-> TODA ENTRADA DEVE SER TRATADA!

'''
print('\n')

'''try:
    num = int(input('Informe um número: '))
    print(f'Valor informado: {num}')
except ValueError as error:
    print(f'Valor informado está incorreto. Confira: {error}')'''

# Outra forma de fazer: --> Utilizando o else

'''try:
    num = int(input('Informe um número: '))
except ValueError as error:
    print(f'Valor informado está incorreto. Confira: {error}')
else:
    print(f'Valor informado: {num}')'''

# O else só é executado caso não ocorra o erro

#========================================================================================================

# Utilização do finally:

'''try:
    num = int(input('Informe um número: '))
except ValueError as error:
    print(f'Valor informado está incorreto. Confira: {error}')
else:
    print(f'Valor informado: {num}')
finally:
    print('Executando o finally')'''

# O finally será executado SEMPRE. Independente de erros ou não.

# O finally, geralmente, é utilizado para fechar ou deslocar recursos. (Estabelecer conexão
# com banco de dados, por exemplo)

#========================================================================================================

# Tratamento recomendado:

def dividir(num1, num2):
    try:
        return float(num1) / float(num2)
    except ValueError as error:
        return f'Valor informado é do tipo incorreto: {error}'
    except ZeroDivisionError as zero:
        return 'Impossível dividir um número por zero.'

n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

print(dividir(n1, n2))

#========================================================================================================

# Tratando o problema de forma genérica:

'''def dividir(num1, num2):
    try:
        return float(num1) / float(num2)
    except:
        return 'Ocorreu um problema.'

n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

print(dividir(n1, n2))'''

#========================================================================================================
print('\n')

# Tratamento Semi-Genérico:

def dividir(num1, num2):
    try:
        return float(num1) / float(num2)
    except (ValueError, ZeroDivisionError) as error:
        return f'Ocorreu um problema. Erro: {error}'

n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

print(dividir(n1, n2))