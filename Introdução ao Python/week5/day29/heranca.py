'''
Herança - (Inheritance)

-> A ideia de herança é a possibilidade de reaproveitar código.
-> Extender as classes


OBS: Com a herança, a partir de uma classe existente, pode-se extender outra classe que passa
a herdar atributos e métodos da classe herdada.
'''
print()

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    contador = 0

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__id = Funcionario.contador + 1
        Funcionario.contador = self.__id

    def nomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

'''
Perceba que tanto em 'Cliente' quanto em 'Funcionario' tem a repetição de atributos do método
construtor (__init__) e do método 'nomeCompleto', isso se chama herança. Se parar para pensar, tanto 
'Cliente' e 'Funcionario' podem ser consideradas do tipo 'Pessoa', por exemplo. Com isso, pode-se
dizer que ambos herdam a característica de uma pessoa.
'''

user = Cliente('Felipe', 'Ribeiro', '123.456.789-00', 1234)
func = Funcionario('Nome', 'Sobrenome', '987.654.321-00')

print(user.nomeCompleto())
print(func.nomeCompleto())
print(func.contador)

print()
#=================================================================================================
# Refatorando as classes:

'''
Quando uma classe herda de outra classe, a classe herdada é conhecida como 'Super Classe',
'Classe Mãe', 'Classe Pai', 'Classe Genérica' ou 'Classe Base'.

Quando uma classe herda de outra classe, a classe que herdou é chamada de 'Sub Classe',
'Classe Filha' ou 'Classe Específica'.
'''

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa): # Herdou a classe 'Pessoa'
    "Cliente herda de Pessoa"

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # o 'super()' permite acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa): # Herdou a classe 'Pessoa'
    "Funcionário herda de Pessoa"

    contador = 0

    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf) # o 'super()' permite acessar a super classe
# ou -> Pessoa.__init__(self, nome, sobrenome, cpf) -> outra forma de acessar a super classe
        self.__id = Funcionario.contador + 1
        Funcionario.contador = self.__id

user1 = Cliente('Felipe', 'Ribeiro', '123.456.789-00', 1234)
func1 = Funcionario('Nome', 'Sobrenome', '987.654.321-00')

print(user1.nomeCompleto())
print(func1.nomeCompleto())
print(func1.contador)

# No método super().__init() são atribuídos os atributos desejados da classe que está...
# ...sendo herdada

print(user1.__dict__)
print(func1.__dict__)

print()
#=================================================================================================
# Sobrescrita de métodos (Overriding)

# Ocorre quando reimplementamos/reescrevemos um método presenta na super classe em...
#... classes filhas

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa): # Herdou a classe 'Pessoa'
    "Cliente herda de Pessoa"

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # o 'super()' permite acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa): # Herdou a classe 'Pessoa'
    "Funcionário herda de Pessoa"

    contador = 0

    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf) # o 'super()' permite acessar a super classe
# ou -> Pessoa.__init__(self, nome, sobrenome, cpf) -> outra forma de acessar a super classe
        self.__id = Funcionario.contador + 1
        Funcionario.contador = self.__id
    
    def nomeCompleto(self): # Método já presente na super classe sendo reescrito adaptado...
        #... à classe Funcionário
        # print(super().nomeCompleto()) -> Acessar a função original da super classe
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__id}. Nome: {self._Pessoa__nome}'

user1 = Cliente('Felipe', 'Ribeiro', '123.456.789-00', 1234)
func1 = Funcionario('Teste', 'Sobrenome', '987.654.321-00')

print(user1.nomeCompleto())
print(func1.nomeCompleto())

# Com o método super() podemos acessar qualquer método da super classe nas classes filhas