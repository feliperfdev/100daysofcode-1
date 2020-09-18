from time import sleep

class Banking:

    contador = 0

    def __init__(self, nome, sobrenome, carteira):
        self.nome = nome
        self.sobrenome = sobrenome
        self.carteira = float(carteira)
        Banking.contador += 1
        self.__id = Banking.contador

    guarda_contas = []
    conta = {}

    def apresentaPessoa(self):
        print(f'\nUsuário: {self.nome} {self.sobrenome}\nID: {self.__id}\n')

    def apagarConta(self):
        num_check = int(input('Informe o número da conta que deseja apagar: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                Banking.guarda_contas.remove(conta)
                Banking.conta.clear()
                print('Conta removida com sucesso!')

    def cadastrar(self):
        Banking.conta['num'] = int(input('Informe o número da sua conta: '))
        Banking.conta['senha'] = input('Informe uma senha para sua conta: ')
        Banking.conta['saldo'] = float(input('Informe o saldo da sua conta: '))
        Banking.guarda_contas.append(Banking.conta)

    def sacar(self):
        num_check = int(input('Informe o número da conta para realizar o saque: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                if Banking.conta['saldo'] > 0:
                    saque = float(input('Informe a quantia que deseja sacar: '))
                    if Banking.conta['saldo'] > saque:
                        Banking.conta['saldo'] -= saque
                        print('Saque realizado com sucesso! Saldo atual: R${}'.format(Banking.conta['saldo']))
                    else:
                        print('O valor informado é superior ao valor disponível em conta ;-; ')
                else:
                    print('Desculpe, mas não há saldo suficiente para ser sacado...')
            return conta
    
    def depositar(self):
        num_check = int(input('Informe o número da conta para realizar o depósito: '))
        senha_check = input('Informe a senha para confirmar: ')
        if num_check == Banking.conta['num'] and senha_check == Banking.conta['senha']:
            for conta in Banking.guarda_contas:
                if self.carteira > 0:
                    depositar = float(input('Informe a quantia que deseja depositar na conta: '))
                    if self.carteira > depositar:
                        self.carteira -= depositar
                        Banking.conta['saldo'] += depositar
                        print('Depósito realizado com sucesso!\nSaldo atual: {}\nValor em carteira: {}'.format(Banking.conta['saldo'], self.carteira))
                    else:
                        print('O valor informado é superior ao valor disponível na sua carteira.')
                else:
                    print('Desculpe, mas não há valor suficiente em sua carteira para ser depositado na conta de número {}'.format(Banking.conta['num']))
            return conta

c1 = Banking('Pessoa', 'Qualquer', 500)
c1.apresentaPessoa()
c1.cadastrar()
c1.sacar()
c1.depositar()

sleep(3.0)