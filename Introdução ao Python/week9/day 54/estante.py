from livros import Livro

class Estante(Livro):
    def __init__(self):
        super().__init__()
    
    estante = []

    def tamanhoEstante(self):
        tamanho = int(input('Quantos livros cabem na estante? '))
    
    def adicionarLivroEstante(self):
        livro = str(input('Informe o nome do livro que deseja adcionar à estante: '))
        if livro == Livro.livros['nome']:
            for book in Livro.listaLivros:
                Estante.estante.append(book)

    def removerLivroEstante(self):
        livro = str(input('Informe o nome do livro que deseja remover da estante: '))
        if livro == Livro.livros['nome']:
            for book in Livro.listaLivros:
                Estante.estante.remove(book)

    def ordenarPorQuantidadePaginas(self):
        pass