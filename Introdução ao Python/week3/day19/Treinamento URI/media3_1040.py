n1, n2, n3, n4 = input().split()
n1 = float(n1)*2; n2 = float(n2)*3; n3 = float(n3)*4; n4 = float(n4)*1


def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4)/10

media = media(n1, n2, n3, n4)

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    novaMedia = (media + exame)/2
    if novaMedia >= 5:
        print('Aluno aprovado.')
    elif novaMedia <= 4.9:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(novaMedia))