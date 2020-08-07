'''
Abstração e Encapsulamento

O grande objetivo da Programação Orientada a Objetos (POO) é encapsular o código dentro de um
grupo lógico e hierarquico utilizando classes.


Abstração, em POO, é o ato de expor apenas os dados relevantes de uma classe, escondendo atributos
e métodos privados do usuário.
'''
print()

class Usuario:

    contador = 0

    @classmethod
    def countUser(cls):
        print(f'Há {cls.contador} usuário(s) no sistema')
    
    def saudacao(self):
        print(f'Bem vindo(a) {self.user}!')

    def __init__(self, user, email, senha):
        self.id = Usuario.contador + 1
        self.user = user
        self.email = email
        self.__senha = senha
        Usuario.contador = self.id
    
    def verifEmail(self, email):
        self.email = email.strip()
        self.email = email.replace(' ', '')
        try:
            assert('@' in self.email)
        except AssertionError:
            print('Email invalido!')
            exit(1)
        else:
            print('Email validado com sucesso!')
    
    def verifSenha(self, senha):
        if len(self.__senha) < 8:
            print('Sua senha é muito fraca!')
            exit(1)
        else:
            print('Senha validada com sucesso!')
    
    def geraUser(self):
        self.verifEmail(self.email)
        self.verifSenha(self.__senha)
        self.saudacao()
        self.countUser()

user = Usuario('Felipe', 'felipeemail@gmail.com', '123456789')
print(user.__dict__)

user.geraUser()

print()
'''user.countUser()
user.verifEmail('felipeemail@gmail.com')
user.verifEmail('felipe  m ail gmail.com')'''

'''user2 = Usuario('Outro', 'emailcorreto@gmail.com', '12345')
user2.geraUser()'''

user2 = Usuario('Outro', 'emailcorreto@gmail.com', 'qwerty1234')
user2.geraUser()