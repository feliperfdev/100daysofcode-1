from time import sleep
import shutil
import os

pasta_contas = 'sua pasta aqui' # caminho do deretório
# atentar para o uso correto do '/'
escolha = ()

def sair():
    "Função para sair do loop do programa"
    print('Saindo do programa...')
    sleep(2.0)
    exit(0)

lista = []
def listarContas(diretorio):
    "Função que lista os arquivos presentes no diretório informado na variável 'pasta_contas'"
    global lista # acessando a variável 'lista', que é uma variável do escopo global
    for index, contas in enumerate(os.listdir(diretorio), start=0): # o 'index' é a variável auxiliar que vai fazer a enumeração dos ID's com a função enumerate()
        lista.append(contas) # adicionando na lista o nome das contas presentes no diretório informado
        print(f'Id: {index} Nome: {contas}', end='\n')
'''
Basicamente, essa função utiliza de uma lista criada no escopo global para poder
armazenar o nome de todos os arquivos do diretório dentro dela. Com isso, o nome de cada arquivo poderá ser acessado através do
índice, esse índice representará o ID informado na variável 'index' criada no loop for.
'''

def remove(caminho, arquivo): # Ainda não está funcionando
    caminhoFinal = r'{}{}'.format(caminho, arquivo)
    if os.path.isfile(caminhoFinal): # verifica se o arquivo existe
        os.remove(caminhoFinal)
        raise PermissionError('\nVocê não tem permissão para remover esse arquivo.')
        raise FileNotFoundError('\nO arquivo informado não foi encontrado.')
        raise ValueError('\nInforme um arquivo válido e existente.')

try:
    while(escolha != 2):
        print('\nO que deseja fazer? ')
        escolha = int(input('\n[1] - Adicionar uma conta\n[2] - Sair do arquivo\n[3] - Listar contas\n[4] - Apagar uma conta (por enquanto só funciona no terminal do python)\n'))
        if (escolha == 1):
            print('--------------------Conta--------------------')
            nome_conta = input('Digite o nome da conta: ')
            print(f'--------------------{nome_conta}--------------------')

            with open(f'{nome_conta}.txt', 'w') as arquivo: # gera o arquivo txt com o nome informado, caso ele não exista
                arquivo.write(f'--------------------{nome_conta}--------------------\n\n')
                nome = str(input('Nome: '))
                arquivo.write(f'Nome: {nome}\n')
                email = str(input('Email: '))
                arquivo.write(f'Email: {email}\n')
                senha = str(input('Senha: '))
                arquivo.write(f'Senha: {senha}\n')
                print('----------------------------------------')
            shutil.move('{}/{}.txt'.format(os.getcwd(), nome_conta), '{}{}.txt'.format(pasta_contas, nome_conta))
            # shutil.move() -> pega o diretório atual com o nome do arquivo txt que foi criado e move para a pasta de contas, gerando o txt lá com o mesmo nome

        if (escolha == 3):
            # esse for vai fazer uma listagem de todos os arquivos contidos na pasta de contas (que serão listados por meio do os.listdir())
            listarContas(pasta_contas)
            inform = int(input('\nDeseja acessar alguma dessas contas? Informe o ID: (Para sair, digite -1) '))
            abrir = open('{}{}'.format(pasta_contas, lista[inform]), 'r')
            # o número informado na variável 'inform' vai direcionar para o índice desejado (que está relacionado ao ID) dentro da lista...
            # O índice 0 da lista corresponde ao ID 0, o índice 1 ao ID 1, e por aí vai. O objetivo é acessar o nome através do ID informado 
            # para que ele seja retornado na variável lista[inform], jogando na função open() e permitindo o acesso ao arquivo desejado
            # OBS: Toda essa explicação vale para todas as outras situações em que utilizou-se a função listarContas() e a variável lista[índice]

            # a variável abrir utiliza a função open na pasta contas para leitura do arquivo informado
            if (inform == -1):
                sair()
            print('===================================================================================')
            print(f'                           Acessando a conta: {lista[inform]}')
            print()
            print(abrir.read()); print() # realiza leitura do arquivo que foi informado
            print('===================================================================================')
            lista.clear() # Limpando a lista para liberar espaço na memória
            sleep(0.2)
        
        if (escolha == 4):
            listarContas(pasta_contas)
            apagar = int(input('\nInforme o ID da conta que deseja apagar: '))
            remove(pasta_contas, lista[apagar]) # apaga o arquivo informado
            print(f'\nA conta: {lista[apagar]} foi apagada.\n')
            lista.clear()

except Exception as error:
    print(f'\nOpa! Aparentemente, ocorreu um erro. {error.__class__}')
    sleep(2.0)

if (escolha == 2):
    sair()