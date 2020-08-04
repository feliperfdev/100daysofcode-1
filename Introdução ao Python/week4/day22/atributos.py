'''
Atributos

-> Representam as características do objeto, ou seja, pelos atributos consegue-se representar
computacionalmente os estados de um objeto

-> Divide-se os atributos em 3 grupos: 
    - Atributos de instância
    - Atributos de classe
    - Atributos dinâmicos
'''
print('\n')

# Atributos de intância: São atributos declarados dentro do método construtor
# Método construtor: É um método especial utilizado para a construção do objeto

# Exemplo:

class Lampada:
    def __init__(self, voltagem, cor): # método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Protudo:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

'''
O que é self?

-> É uma forma de dizer que é o próprio objeto que está executando o método

-> Por convenção, utiliza-se o 'self'. Mas pode ser outro nome.
'''

#==================================================================================================

# Atributos públicos e privados:
'''
Por convenção, é estabelecido que todo atributo de uma classe é público, ou seja, pode ser
acessado em todo o projeto.


Atributos privados utilizam um duplo underline (__) antes do nome -> 'self.__nome' -> 
isso significa que o atributo nome é do tipo private
Isso é conhecido como Name Mangling
'''

class Acesso:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.email = email
        self.__senha = senha
    
    def mostraSenha(self):
        print(self.__senha)

user = Acesso('Felipe', 'user@gmail.com', '12345678')

print(user.email);                                                          print('\n')
#print(user.__nome) --> AtributteError
#print(user.__senha) --> AtributteError

print(dir(user));                                                           print('\n')

# Acessando atributos privados:
print(user._Acesso__nome)
print(user._Acesso__senha);                                                 print('\n')
# Isso é o Name Mangling

#==================================================================================================

# O que significa atributos de instância:
'''
Significa que ao criar instâncias/objetos de uma classe, todas as instâncias terão
estes atributos
'''

user2 = Acesso('Alguem', 'email@gmail.com', '9876543210')
user3 = Acesso('Outro', 'novoemail@gmail.com', '23344466666')

user2.mostraSenha()
user3.mostraSenha()

p1 = Protudo('XBox', 'videogame', 2000)
p2 = Protudo('Playstation', 'videogame', 3000)

print('\n')
#======================================================================================================

# Atributos de Classe:

# Atributos de classe são atributos declarados diretamente na classe, ou seja, fora do construtor.
# Geralmente, já se inicializa um valor, esse valor é compartilhado entre todas as instâncias...
#... da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores, como é o...
#... caso dos atributos de instância, com os atributos de classe todas as instâncias terão o...
#... mesmo valor para este atributo

# Refatorando a classe Produto:

class Protudo:

    imposto = 1.05 # 0.05% de imposto # Atributo de classe
    cont = 0 # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.id = Protudo.cont + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Protudo.imposto)
        Protudo.cont = self.id # faz a atualização de id

p3 = Protudo('iPhone', 'Celular', 8000)
p4 = Protudo('Xiaomi', 'Celular', 2500)
print(p3.imposto) # acessando um atributo de classe sem precisar criar uma instância para ele
print(p4.imposto)

print(p3.valor) # O imposto foi aplicado ao valor dentro do 'self.valor'
print(p4.valor)

# Não é necessário criar uma instância da classe para fazer acesso a um atributo de classe

print(p3.id) # id 1
print(p4.id) # id 2

print('\n')
#======================================================================================================

# Atributos Dinâmicos:

# É um atributo de instância que pode ser criado em tempo de execução
# OBS: O Atributo Dinâmico será exclusivo da instância que o criou

class Protudo:

    imposto = 1.05 # 0.05% de imposto # Atributo de classe
    cont = 0 # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.id = Protudo.cont + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Protudo.imposto)
        Protudo.cont = self.id # faz a atualização de id

produtoUm = Protudo('Caneta', 'escreve', 5.0)
produtoDois = Protudo('Lápis', 'escreve', 3.0)

produtoUm.peso = '5g' # só vai existir para o 'produtoUm'. É criado em tempo de execução

print(f'Nome: {produtoUm.nome}, Descrição: {produtoUm.descricao}, Valor: {produtoUm.valor}, Peso: {produtoUm.peso}')

#print(f'Peso produtoDois: {produtoDois.peso}') # Não existe / Não foi criado -> AtributteError

print(produtoUm.__dict__)
print(produtoDois.__dict__);                                            print('\n')
print(Protudo.__dict__)

print('\n')
# Deletando atributos:

# utilizando a palavra reservada 'del'

del produtoUm.peso
print(produtoUm.__dict__)

del produtoUm.descricao
print(produtoUm.__dict__)