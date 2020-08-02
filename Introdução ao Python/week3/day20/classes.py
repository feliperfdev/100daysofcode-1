'''
Classes (POO)

--> São modelos de objetos do mundo real sendo representados computacionalmente

# Funções dentro da classe são chamadas de métodos

As classes podem conter:
    -> Métodos: representam os comportamentos do objeto. Ou seja, as ações que esse objeto pode
    realizar no seu sistema
    -> Atributos: representam as características do objeto. Ou seja, pelos atributos se consegue
    representar computacionalmente os estados de um objeto.

OBS: Quando se nomeia uma classe em Python, por convenção, utiliza-se a inicial com caixa alta.
Se o nome for composto, utiliza-se as inicias de ambas as palavras em caixa alta, todas juntas.
'''
print('\n')

class Teste:
    pass

# O 'pass' é utilizado quando o bloco de código ainda não está definido

class Circuito:
    def ligar(circuit):
        circuit = 1
        print('Circuito ligado')
    def desligar(circuit):
        circuit = 0
        print('Circuito desligado')

c1 = Circuito()
c1.ligar()
c1.desligar()