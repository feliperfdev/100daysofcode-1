from time import sleep

class Banking:

    contador = 0
    guarda_contas = []
    conta = {}
    arquivo = open('historico.txt', 'w+')

    @classmethod # Decorator
    def countUser(cls): # cls --> índica a classe -> necessita do decorator @classmethod
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def loadBar():
        bar = '===========================\n'
        for i in range(len(bar)):
            print(bar[i], end='', flush=True)
            sleep(0.05)

    @staticmethod
    def apagarConta():
        """Apaga a conta"""
        num_check = int(input('Informe o número da conta que deseja apagar: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                Banking.guarda_contas.remove(conta)
                print('\nApagando...')
                Banking.loadBar()
                Banking.conta.clear()
                print('Conta removida com sucesso!')

    def __init__(self, nome, sobrenome, carteira):
        self.nome = nome
        self.sobrenome = sobrenome
        self.carteira = float(carteira)
        Banking.contador += 1
        self.__id = Banking.contador

    @classmethod
    def hist(cls):
        Banking.arquivo.write('-=-=-=-=-=-=-=- HISTORICO -=-=-=-=-=-=-=-\n')

    def apresentaPessoa(self):
        """Apresentação do usuário"""
        print(f'\nBem vindo(a)!\nUsuário: {self.nome} {self.sobrenome}\nID: {self.__id}\n')


    def statusConta(self):
        """Mostra Status da Conta"""
        print('\n===================================')
        print('Número da conta: {}\nValor disponível em conta: {}\nValor disponível na carteira: {}'.format(Banking.conta['num'], Banking.conta['saldo'], self.carteira))
        print('===================================\n')

    def cadastrar(self):
        """Realiza o cadastro do usuário
        Guarda informações em dict(conta)\n
        -> Banking.conta['num']\n
        -> Banking.conta['senha']\n
        -> Banking.conta['saldo']\n
        Guarda o dicionário com as informações salvas em list(guarda_contas)\n
        -> Banking.guarda_contas
        """
        Banking.conta['num'] = int(input('Informe o número da sua conta: '))
        Banking.conta['senha'] = input('Informe uma senha para sua conta: ')
        Banking.conta['saldo'] = float(input('Informe o saldo da sua conta: '))
        Banking.loadBar()
        Banking.guarda_contas.append(Banking.conta)
        print('Cadastro da conta {} realizado com sucesso!\n'.format(Banking.conta['num']))

    def sacar(self):
        """Realizar saque da quantia determinada na conta."""
        Banking.statusConta(self)
        num_check = int(input('Informe o número da conta para realizar o saque: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                if Banking.conta['saldo'] > 0:
                    saque = float(input('Informe a quantia que deseja sacar: '))
                    if Banking.conta['saldo'] >= saque:
                        print('\nRealizando saque...')
                        Banking.loadBar()
                        Banking.conta['saldo'] -= saque
                        self.carteira += saque
                        print('Saque realizado com sucesso! Saldo atual: R${}'.format(Banking.conta['saldo']))
                        Banking.arquivo.write('Sacou: R${} --------- Saldo: R${}\n'.format(saque, Banking.conta['saldo']))
                        Banking.statusConta(self)
                    else:
                        print('O valor informado é superior ao valor disponível em conta ;-; ')
                else:
                    print('Desculpe, mas não há saldo suficiente para ser sacado...')
            return conta
    
    def depositar(self):
        """Realizar depósito da quantia determinada na conta."""
        Banking.statusConta(self)
        num_check = int(input('Informe o número da conta para realizar o depósito: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                if self.carteira > 0:
                    depositarV = float(input('Informe a quantia que deseja depositar na conta: '))
                    if self.carteira >= depositarV:
                        print('\nRealizando depósito...')
                        Banking.loadBar()
                        self.carteira -= depositarV
                        Banking.conta['saldo'] += depositarV
                        print('Depósito realizado com sucesso!\nSaldo atual: {}\nValor em carteira: {}'.format(Banking.conta['saldo'], self.carteira))
                        Banking.arquivo.write('Depositou: R${} --------- Saldo: R${}\n'.format(depositarV, Banking.conta['saldo']))
                        Banking.statusConta(self)
                    else:
                        print('O valor informado é superior ao valor disponível na sua carteira.')
                else:
                    print('Desculpe, mas não há valor suficiente em sua carteira para ser depositado na conta de número {}'.format(Banking.conta['num']))
            return conta

def menu(user, options):
    if options == 1:
        user.sacar()
    if options == 2:
        user.depositar()
    if options == 3:
        user.apagarConta()
        inicia()
    if options == 4:
        print(Banking.arquivo.read())
    if options == 5:
        Banking.arquivo.write('-=-=-=-=-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-')
        print('Saindo...')
        sleep(0.5)
        exit(1)

def inicia():
    cadastro = ()
    while 1: # while True
        cadastro = input('Deseja se cadastrar [SIM] [NÃO] ? ')
        respotaPos = ['sim', 'SIM', 's', 'S', 'Sim']
        respostaNeg = ['nao', 'não', 'n', 'N', 'Nao', 'Não']
        if cadastro in respotaPos:
            nome, sobrenome = input('Nome completo: ').split()
            carteira = float(input('Valor em carteira: '))
            Banking.arquivo.write('User: {} {}\n\n'.format(nome, sobrenome))
            user = Banking(nome, sobrenome, carteira)
            user.apresentaPessoa()
            user.cadastrar()
            Banking.hist()
            break
        elif cadastro in respostaNeg:
            exit(1)
    options = ()
    while options != 5:
        options = int(input('O que deseja fazer?\n[1] - Sacar\n[2] - Depositar\n[3] - Apagar conta\n[4] - Ver histórico (não funciona)\n[5] - Sair\n'))
        menu(user, options)

if __name__ == '__main__':
    inicia()

sleep(3.0)