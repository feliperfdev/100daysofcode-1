'''
Debuggando no Python


'''
print('\n')

# A utilização do print() para debugar código é uma prática ruim.

'''def dividir(num1, num2):
    print(f'Num1 = {num1}, Num2 = {num2}')
    try:
        return float(num1) / float(num2)
    except ValueError as error:
        return f'Valor informado é do tipo incorreto: {error}'
    except ZeroDivisionError as zero:
        return 'Impossível dividir um número por zero.'

n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

print(dividir(n1, n2))'''

# Existem formas mais profissionais de fazer o debugg do código.


def dividir(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return float(num1) / float(num2)
    except ValueError as error:
        return f'Valor informado é do tipo incorreto: {error}'
    except ZeroDivisionError as zero:
        return 'Impossível dividir um número por zero.'

n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

print(dividir(n1, n2))


#Para debuggar:

'''
1 -> Selecionar uma linha, clicar com o botão direito e colocar um 'breakpoint' de início
2 -> Selecionar uma outra linha para colocar um 'breakpoint' de chegada
OBS: Pode haver mais de dois breakpoints
OBS 2: Os breakpoints servem para escolher uma parte específica do código para ser debuggada
3 -> No VSCode, basta ir na aba 'Run' e clicar em 'Start Debugging' depois em 'Python File'
4 -> Utilizar os botões na aba que vai aparecer para ir analisando o código durante o debugging
5 -> Ir fazendo os testes durante as análises.
6 -> Ir verificando os tipos de variáveis que vão saindo, a ordem que o código está sendo executado
7 -> Repetir o processo de debugging até sentir segurança no funcionamento daquela parte do código
'''

#========================================================================================================
