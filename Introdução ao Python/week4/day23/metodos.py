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

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
    
    def nomeCompleto(self):
        "Retorna o nome completo do usuário"
        return f'{self.__nome} {self.__sobrenome}'
    
    def checaEmail(self):
        self.__email = self.__email.strip()
        self.__email = self.__email.replace(' ', '')
        try:
            assert('@' in self.__email)
        except AssertionError:
            return 'Email invalido!'
        return self.__email
    
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
print(novoUser.checaEmail())

print()

outroUser = Usuario('Outro', 'Usuário', 'outro usergm   a il .com', 'umdoistresquatro')
print(outroUser.checaEmail())