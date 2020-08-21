'''
POO - Propriedades

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são chamados
de 'getters' e 'setters'. Os getters retornam o valor do atributo e os setters alteram o valor
do mesmo.

'''
print()

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__id = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__id

    def extrato(self):
        print(f'O cliente {self.__titular} tem R${self.__saldo}.00 de saldo!')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    # Funções para acesso (getters e setters):

    def getSaldo(self):
        return self.__saldo
    
    def getTitular(self):
        return self.__titular
    
    def setTitular(self, titular):
        self.__titular = titular

    def getId(self):
        return self.__id
    
    def getLimite(self):
        return self.__limite
    
    def setLimite(self, limite):
        self.__limite = limite
    
c1 = Conta('Felipe', 4000, 10000)
c2 = Conta('Cesar', 5000, 15000)

c1.extrato()
c2.extrato()

c1.depositar(1000)
c1.extrato()

c1.sacar(3000)
c1.extrato()
c2.transferir(4500, c1)
c1.extrato()
c2.extrato();                                                           print()

soma = c1._Conta__saldo + c2._Conta__saldo
print(f'Soma dos saldos: R${soma}.00')
'''
Perceba que foi acessado o saldo, mesmo ele sendo um atributo do tipo privado. Isso é possível,
porém, não é o que seria recomendado. Afinal, se é privado, não deveria ser acessado. Então,
para o bem da empresa ou até mesmo do cliente, esse tipo de coisa não deve ser feita.
'''

# O que fazer então para poder acessar o saldo sem ser dessa maneira?
# Criaremos funções dentro da classe para tornar isso possível, sem prejudicar a empresa ou cliente.
print()

soma = c1.getSaldo() + c2.getSaldo()
print(f'Soma dos saldos: R${soma}.00')

print(f'Id Conta 1: {c1.getId()}\nId Conta 2: {c2.getId()}');                   print()

print(f'Limite atual de {c1.getTitular()} -> R${c1.getLimite()}.00')
c1.setLimite(20000)
print(f'Novo limite de {c1.getTitular()} -> R${c1.getLimite()}.00')

#=================================================================================================
print()

'''
No entanto, utilizar funções como 'getFuncao' ou 'setFuncao' está mais relacionado à linguagens
como Java. Em Python, podemos utilizar decorators para facilitar a criação dos métodos de
manipulação. Sendo o @property para criar os getters e o @nomeGetter.setter para o setter.
'''

# Refatorando a classe:

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__id = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__id

    def extrato(self):
        print(f'O cliente {self.__titular} tem R${self.__saldo}.00 de saldo!')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    # Funções para acesso (getters e setters):

    @property # definindo um getter
    def limite(self):
        return self.__limite

    @limite.setter # definindo o setter --> nomeDoGetter.setter
    def limite(self, value):
        if isinstance(value, str):
            value = float(value)
            self.__limite = float(value)
        self.__limite = float(value)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            valor = float(valor)
            self.__saldo = float(valor)
        self.__saldo = float(valor)
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, name):
        if isinstance(name, str):
            self.__titular = name
    
    @property
    def idNumero(self):
        return self.__id
    
    @property
    def valorTotal(self):
        return self.__saldo + self.__limite

conta1 = Conta('Felipe', 4000, 10000)
conta2 = Conta('Camila', 7000, 25000)

# print(conta1.__dict__)

somaSaldos = conta1.saldo + conta2.saldo 
# Perceba que, para os getters, não é necessário parênteses.
print(f'Soma dos saldos: {somaSaldos}');                                        print()

print(f'Limite de {conta1.titular}: R${conta1.limite}.00')
print(f'Limite de {conta2.titular}: R${conta2.limite}.00')

print(f'Valor total Conta 1: {conta1.valorTotal}')
print(f'Valor total Conta 2: {conta2.valorTotal}');                             print()

print(conta1.titular)
print(conta2.titular)

conta3 = Conta('Alguma Pessoa', '3000', '9000')
print(f'Total: {conta3.saldo + conta3.limite}')