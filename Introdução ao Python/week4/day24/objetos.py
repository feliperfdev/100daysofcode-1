'''
Objetos

--> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua repre-
sentação computacional, devemos poder criar quantos objetos forem necessários. Pode-se pensar
nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

'''
print()

class Lampada:
    def __init__(self, voltagem, cor, luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False
    
    def checaLampada(self):
        if self.__ligada is False:
            return 'Lâmpada desligada'
        return 'Lâmpada ligada'

class Usuario:

    contador = 0
    
    @classmethod
    def countUser(cls):
        return f'{cls.contador} usuário(s)'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id
    
    def nomeCompleto(self, nome, sobrenome):
        nome = self.__nome
        sobrenome = self.__sobrenome
        return f'{nome} {sobrenome}'
    
    def checaEmail(self, email):
        self.__email = email.strip()
        self.__email = email.replace(' ', '')
        try:
            assert('@' in self.__email)
        except AssertionError:
            return 'Email invalido!'
        else:
            return 'Email validado com sucesso!'

# O 'lamp1' é um objeto/intância
lamp1 = Lampada(110, 'branca', 50)
print(lamp1.checaLampada());                                            print()


nome = 'Felipe'
sobrenome = 'Ribeiro'
email = 'felipeemail@gmail.com'
senha = '123456789'

user1 = Usuario(nome, sobrenome, email, senha)
print(user1.nomeCompleto(nome, sobrenome))
print(user1.checaEmail(email))
print(user1.contador)
print(user1.countUser())