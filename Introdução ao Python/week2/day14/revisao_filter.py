print('\n')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda num: num%2==0, lista)))

print(list(filter(lambda num: num%2!=0, lista)))

print('\n')
#========================================================================================================

cores = 'Vermelho', 'Amarelo', 'Preto', 'Verde', 'Azul', 'Cinza', 'Branco', 'Rosa'

print(list(filter(lambda cor: cor[0]=='V', cores)))

print(list(filter(lambda cor: len(cor)==5, cores)))

print(list(filter(lambda cor: cor[-1]=='o', cores)))