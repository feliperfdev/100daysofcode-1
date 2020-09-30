class Livro:

    idLivro = 0
    paginaAtual = 0
    paginasRestantes = 0
    livros = {}
    listaLivros = []

    def __init__(self):
        self.id = Livro.idLivro + 1
        Livro.idLivro = self.id
        Livro.livros['nome'] = str(input('Título do livro: '))
        Livro.livros['paginas'] = int(input('Total de páginas: '))
        print('Livro {} registrado com sucesso! ID: {}'.format(Livro.livros['nome'], Livro.idLivro))
        Livro.listaLivros.append(Livro.livros)

    def registrarLeitura(self):
        livro = str(input('Nome do livro que deseja registrar uma leitura: '))
        if livro == Livro.livros['nome']:
            for book in self.listaLivros:
                    self.paginaAtual = int(input('Registre a página atual da sua leitura: '))
                    self.paginasRestantes = Livro.livros['paginas'] - self.paginaAtual
                    print('Leitura do livro {} registrada com sucesso!'.format(Livro.livros['nome']))
                    self.porcentagemLeitura()
        else:
            print('Você não tem esse livro cadastrado ;-;')
    
    def loadBar(self, value):
        for i in range(0, 1):
            print('[', end='')
            for j in range(0, round(value)):
                print('|', end='')
            print('] {:.2f}%'.format(value))

    def porcentagemLeitura(self):
        valor = 100 - (self.paginasRestantes/self.paginas)*100
        if valor < 0:
            print('Impossível ler uma quantidade negativa de páginas ;-;')
        elif valor == 0:
            print('Você ainda não leu nada do livro ;-;')
            self.loadBar(valor)
        elif valor < 100:
            print('Você já leu {:.2f}% do livro {}'.format(valor, self.nome))
            self.loadBar(valor)
        elif valor == 100:
            print('Parabéns!! Você leu {:.2f}% do livro {}'.format(valor, self.nome))
            self.loadBar(valor)
        elif valor > 100:
            print('Impossível você ler mais páginas que o total existente nesse livro ;-;')
        

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
        if livro == Livro.livros['nome']:
            print('================================================')
            print('ID: {}'.format(Livro.idLivro))
            print('Título: {}'.format(self.nome))
            print('Páginas lidas: {} ({:.2f}%)'.format(self.paginaAtual, (100 - (self.paginasRestantes/self.paginas)*100)))
            print('Comentário/Resenha:\n{}'.format(self.comentario))
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
    while 1:
        registro = str(input('Deseja registrar algum livro? '))
        if registro == 'sim' or registro == 'SIM' or registro == 's' or registro == 'S' or registro == 'Sim':
            cadastro = int(input('\nDeseja cadastrar quantos livros? '))
            for i in range(1, cadastro+1):
                livro = Livro()
        elif registro == 'nao' or registro == 'não' or registro == 'n' or registro == 'N' or registro == 'NAO' or registro == 'Não' or registro == 'NÃO':
            exit(1)
        acoes(livro)


if __name__ == '__main__':
    menu()