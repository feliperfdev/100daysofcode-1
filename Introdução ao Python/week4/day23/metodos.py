'''
Métodos ---> (Funções)

-> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar
no sistema

Divide-se métodos em 2 grupos:
    - Métodos de Instância
    - Métodos de Classe

# O método __init__ é um método especial chamado de 'construtor'. Sua função é construir o
objeto a partir da classe ---> OBS: Lê-se 'dunder init'.

OBS: Os métodos 'dunder' no python são chamados de métodos mágicos

OBS: É possível criar um método 'dunder' por conta própria, porém não é aconselhado.
'''
print()

# >>>>>>>>>> Métodos de instância <<<<<<<<<

# Uma classe pode possuir quantos métodos forem necessários

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class Produtos:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produtos.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = (Produtos.imposto * valor)
        Produtos.contador = self.__id
    
    def desconto(self, porcentagem):
        "Retorna o valor do produto com o desconto aplicado"
        return f'Valor anterior: {self.__valor}\nNovo valor: {(self.__valor * (100 - porcentagem))/100}'

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
    
    def nomeCompleto(self):
        "Retorna o nome completo do usuário"
        return f'{self.__nome} {self.__sobrenome}'
    
    def checaEmail(self, email):
        self.__email = email.strip()
        self.__email = email.replace(' ', '')
        try:
            assert('@' in self.__email)
        except AssertionError:
            return False
            exit(1)
        return True
    
    def checaSenha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    '''def __deslog__(self, verif, senha): # Não é aconselhável criar um método 'dunder'
        print(f'Verificando: {verif}, Senha: {senha}')'''

#===============================================================================================

prod1 = Produtos('XBox One S', 'Console - Microsoft', 2000)
print(prod1.desconto(20)) # 20% de desconto

user1 = Usuario('Felipe', 'Ribeiro', 'email@gmail.com', '123456789');               print()
print(user1.nomeCompleto())

user2 = Usuario('Pessoa', 'Qualquer', 'mail1@gmail.com', '543211234')
print(user2.nomeCompleto())

print(Usuario.nomeCompleto(user1)) # -> Outra forma de acessar o método

print(f'Senha User1: {user1._Usuario__senha}') # Acesso de forma errada, mesmo que funcione

print()

novoUser = Usuario('User', 'sobrenomeUser', 'user   @gmail. com', '23344466666')
#print(novoUser.checaEmail('user   @gmail. com'))

print()

outroUser = Usuario('Outro', 'Usuário', 'outro usergm   a il .com', 'umdoistresquatro')
#print(outroUser.checaEmail('outro usergm   a il .com'))
#print(outroUser.checaSenha('1234'))
print(outroUser.checaSenha('umdoistresquatro'))

print()
#===============================================================================================

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
email = input('Email: ')
senha = input('Senha: ')
confirmSenha = input('Confirme sua senha: ');                               print()

if senha == confirmSenha:
    newUser = Usuario(nome, sobrenome, email, senha)

else:
    print('Senha não confere.')
    exit(1)

if newUser.checaEmail(email):
    pass
else:
    print('Acesso negado!')
    exit(1)

if newUser.checaSenha(senha):
    print('Acesso permitido!')
    print(f'Senha criptografada: {newUser._Usuario__senha}')
else:
    print('Acesso negado!')

print()
#===============================================================================================

# >>>>>>>>>> Métodos de Classe <<<<<<<<<

# Utilizam decorators

'''
Em métodos de classe, não se faz acesso aos atributos de instância (que utilizam o self),
eles fazem acesso à classe. São conhecidos como métodos estáticos em outras linguagens.
'''

class Usuario:

    contador = 0
    @classmethod # Decorator
    def countUser(cls): # cls --> índica a classe -> necessita do decorator @classmethod
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id
        print(f'Usuário criado: {self.__geraUsuario()}')
    
    def nomeCompleto(self):
        "Retorna o nome completo do usuário"
        return f'{self.__nome} {self.__sobrenome}'
    
    def checaEmail(self, email):
        self.__email = email.strip()
        self.__email = email.replace(' ', '')
        try:
            assert('@' in self.__email)
        except AssertionError:
            return False
        return True
    
    def checaSenha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __geraUsuario(self): # Método privado (por causa do double underline '__')
        return self.__email.split('@')[0]


newUser = Usuario('Felipe', 'Ribeiro', 'felipe02@gmail.com', '123456789');          print()
Usuario.countUser() # Forma correta
newUser.countUser() # Possível, porém incorreto

print(newUser._Usuario__geraUsuario()) # Acesso de forma ruim

print()
#===============================================================================================

# >>>>>>>>>> Métodos Estáticos <<<<<<<<<

# Utiliza um outro decorador ---> @staticmethod

class Usuario:

    contador = 0
    @classmethod # Decorator
    def countUser(cls): # cls --> índica a classe -> necessita do decorator @classmethod
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao(): # Não recebe nenhum parâmetro de instância ou classe
        return '1234'

    def __init__(self, nome, sobrenome, email, senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id
        print(f'Usuário criado: {self.__geraUsuario()}')
    
    def nomeCompleto(self):
        "Retorna o nome completo do usuário"
        return f'{self.__nome} {self.__sobrenome}'
    
    def checaEmail(self, email):
        self.__email = email.strip()
        self.__email = email.replace(' ', '')
        try:
            assert('@' in self.__email)
        except AssertionError:
            return False
        return True
    
    def checaSenha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __geraUsuario(self): # Método privado (por causa do double underline '__')
        return self.__email.split('@')[0]

novoUsuario = Usuario('Felipe', 'Ribeiro', 'felipemail@gmail.com', '123456789')
print(novoUsuario.definicao())
print(novoUsuario.contador)

print()

outroUsuario = Usuario('Alguem', 'Qualquer', 'qualqueremail@gmail.com', '987654321')
print(outroUsuario.definicao())
print(outroUsuario.contador)

#===============================================================================================
