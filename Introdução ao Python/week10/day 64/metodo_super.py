'''
O método super() -> Herança em POO

-> Se refere à 'super' classe (Classe pai).


'''

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especia = especie

    def fazer_som(self, som):
        print(f'O {self.__nome} faz {som}')
    
    def anda(self, passos):
        print(f'O {self.__nome} andou {passos} passos para frente')

class Cachorro(Animal): # Classe filha
    def __init__(self, nome, especie, raça):
        super().__init__(nome, especie)
        self.__raça = raça

rex = Cachorro('Rex', 'Canino', 'Golden Retriever')
rex.fazer_som('woof woof')
rex.anda(10)

class Gato(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)
    
felix = Gato('Felix', 'Felino')
felix.fazer_som('miau')
felix.anda(4)