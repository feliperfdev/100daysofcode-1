av1 = 0
av2 = 0

def media(av1, av2):
    return (av1+av2)/2

def validacao():

    av1 = float(input())
    while av1 > 10 or av1 < 0:
        print('nota invalida')
        av1 = float(input())

    av2 = float(input())
    while av2 > 10 or av2 < 0:
        print('nota invalida')
        av2 = float(input())

    print('media = {:.2f}'.format(media(av1, av2)))

validacao()

nc = 0
while nc!=2 or nc>2 or nc<1:
    nc = int(input('novo calculo (1-sim 2-nao)'))
    if nc == 1:
        validacao()
    if nc == 2:
        break