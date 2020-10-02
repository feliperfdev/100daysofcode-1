'''
Exercício 4 da Seção 16 do curso de Python
'''

class Televisao:

    volumeChange = 0
    channelChange = 0

    def __init__(self, volume, canal):
        self.volume = volume + Televisao.volumeChange
        self.canal = canal + Televisao.channelChange
        Televisao.volumeChange = self.volume
        Televisao.channelChange = self.canal

class ControleRemoto(Televisao):
    def __init__(self, volume, canal):
        super().__init__(volume, canal)

    def mudaVolume(self, escolha):
        if escolha == 0:
            self.volume = Televisao.volumeChange -1
        elif escolha == 1:
            self.volume = Televisao.volumeChange + 1
        if self.volume < 0:
            self.volume = 0
        elif self.volume >= 80:
            print('Ultrapassar o volume de 80 decibéis seria arriscado para sua saúde!')
            self.volume = 80
        print(f'Volume atual: {self.volume}')
        Televisao.volumeChange = self.volume

    def mudaCanal(self, mudar, escolha=None):
        if mudar == 0: # volta canal em 1 unidade
            self.canal = Televisao.channelChange -1
        elif mudar == 1: # passa o canal para frente em 1 unidade
            self.canal = Televisao.channelChange + 1
        elif mudar == 2: 
        # permite você utilizar a variável 'escolha' para selecionar qualquer canal
            self.canal = escolha
        if self.canal < 0:
            self.canal = 0
        print(f'Canal atual: {self.canal}')
        Televisao.channelChange = self.canal
    
    def mostraVolume(self):
        print(f'Volume: {Televisao.volumeChange}')
    
    def mostraCanal(self):
        print(f'Canal: {Televisao.channelChange}')

tv1 = ControleRemoto(0, 1)
tv1.mudaCanal(2, 32)
tv1.mudaCanal(1)
tv1.mudaVolume(1)
tv1.mudaCanal(0)
tv1.mudaVolume(1)
tv1.mudaCanal(2, 10)
tv1.mudaCanal(0)
tv1.mudaVolume(1)
tv1.mudaCanal(0)
tv1.mudaVolume(1)
tv1.mudaVolume(1)
tv1.mudaVolume(0)