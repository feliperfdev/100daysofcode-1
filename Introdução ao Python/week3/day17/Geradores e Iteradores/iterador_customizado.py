'''
Escrevendo um Iterador Customizado
'''
print('\n')

# Relembrando o uso do range():
print([x for x in range(11)])

#========================================================================================================

# Usando Orientação a Objetos

class Contador:
    def __init__(self, menor, maior): # Funções dentro de uma classe são chamadas de métodos
        super().__init__()
        self.menor = menor
        self.maior = maior
    def __iter__(self): # Vai permitir a utilização da função iter()
        return self
    def __next__(self): # Vai permitir a utilização da função next()
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        else:
            raise StopIteration


# O def __init__ é uma função conhecida como 'construtor' e é responsável por criar os objetos...
#... a partir da classe

cont = Contador(1, 6)
print(cont)
print(cont.menor)
print(cont.maior); print('\n')

itcont = iter(cont)
print(next(itcont))
print(next(itcont))
print(next(itcont))
print(next(itcont))
print(next(itcont));                                                    print('\n')

print([x for x in Contador(1, 34)]) # Réplica do range()