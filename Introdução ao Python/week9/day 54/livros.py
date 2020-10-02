from time import sleep
from math import *

class Livro:

    idLivro = 0
    paginaAtual = 0
    paginasRestantes = 0
    livros = {}
    listaLivros = []

    infoTec = {}.fromkeys(['Ano', 'Autor(a)', 'Edição'], 'desconhecido')

    def __init__(self):
        self.id = Livro.idLivro + 1
        self.comentario = ''
        Livro.idLivro = self.id
        Livro.registraLivro()

    def registraLivro(self):
        self.idLivro = self.id
        self.livros['nome'] = str(input('Título do livro: '))
        self.livros['paginas'] = int(input('Total de páginas: '))
        print('Livro {} registrado com sucesso! ID: {}'.format(self.livros['nome'], self.idLivro))
        self.listaLivros.append(self.livros)

    def registrarLeitura(self):
        livro = str(input('Nome do livro que deseja registrar uma leitura: '))
        if livro == self.livros['nome']:
            for book in self.listaLivros:
                self.paginaAtual = int(input('Registre a página atual da sua leitura: '))
                self.paginasRestantes = self.livros['paginas'] - self.paginaAtual
                print('Leitura do livro {} registrada com sucesso!'.format(self.livros['nome']))
                self.__porcentagemLeitura()
        else:
            print('Você não tem esse livro cadastrado ;-;')
    
    def __loadBar(self, value):
        for i in range(0, 1):
            print('[', end='')
            for j in range(0, round(value)):
                print('|', end='')
            print('] {:.2f}%'.format(value))

    def __porcentagemLeitura(self):
        valor = 100 - (self.paginasRestantes/self.livros['paginas'])*100
        if valor < 0:
            print('Impossível ler uma quantidade negativa de páginas ;-;')
        elif valor == 0:
            print('Você ainda não leu nada do livro ;-;')
            self.__loadBar(valor)
        elif valor < 100:
            print('Você já leu {:.2f}% do livro {}'.format(valor, self.livros['nome']))
            self.__loadBar(valor)
        elif valor == 100:
            print('Parabéns!! Você leu {:.2f}% do livro {}'.format(valor, self.livros['nome']))
            self.__loadBar(valor)
        elif valor > 100:
            print('Impossível você ler mais páginas que o total existente nesse livro ;-;')
        
    def __porcentagemApenas(self):
        valor = 100 - (self.paginasRestantes/self.livros['paginas'])*100
        if self.paginaAtual == 0:
            valor = 0
        return valor
        

    def addComentarioLivro(self):
        livro = str(input('Digite o nome do livro que deseja adicionar um comentário: '))
        for book in self.listaLivros:
            if livro == Livro.livros['nome']:
                Livro.livros['comentario'] = str(input('Comentário/Resenha: '))
                self.comentario = Livro.livros['comentario']
            else:
                print('Você não tem esse livro cadastrado ;-;')
    
    def mostraDadosLivros(self):
        livro = str(input('Informe o livro que deseja visualizar os dados: '))
        if livro == self.livros['nome']:
            print('================================================')
            print('ID: {}'.format(self.idLivro))
            print('Título: {}'.format(self.livros['nome']))
            print('Páginas lidas: {} ({:.2f}%)'.format(self.paginaAtual, self.__porcentagemApenas()))
            print('Comentário/Resenha:\n"{}"'.format(self.comentario))
            print('================================================\n')

def acoes(l):
    action = 0
    while action != 4:
        print('\n[1] - Atualizar histórico de leitura\n[2] - Adicionar uma resenha\n[3] - Mostrar dados de um livro\n[4] - Sair\n')
        action = int(input('O que deseja fazer? '))
        if action == 1:
            l.registrarLeitura()
        if action == 2:
            l.addComentarioLivro()
        if action == 3:
            l.mostraDadosLivros()
        if action == 4:
            exit(1)

def menu():    
    respotaPos = ['sim', 'SIM', 's', 'S', 'Sim']
    respostaNeg = ['nao', 'não', 'n', 'N', 'Nao', 'Não']   
    while 1:
        registro = str(input('Deseja registrar algum livro? '))
        if registro in respotaPos:
            livro = Livro()
        elif registro in respostaNeg:
            exit(1)
        acoes(livro)

if __name__ == '__main__':
    try:
        menu()
    except Exception:
        exit(1)