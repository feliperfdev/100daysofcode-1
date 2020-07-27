def pegaIndiceMeio(iteravel):
    "Função que retorna o índice do meio em um iterável de tamanho ímpar!"
    try:
        assert(len(iteravel)%2 != 0)
        indice = len(iteravel) / 2
        indice = int(indice)
    except (TypeError, ValueError, IndexError, AssertionError) as error:
        return f'Ocorreu um erro na análise desse iterável: {error.__class__}'
    else:
        return iteravel[indice]

print('\n')

lista = [1, 2, 3, 4, 5, 6, 7]

print(pegaIndiceMeio(lista))

print(pegaIndiceMeio((1, 2, 3, 4, 5, 6)))

print(pegaIndiceMeio(range(0, 11)))