dias = int(input())
ano = 0
meses = 0

while dias >= 30:
    if dias >= 30:
        meses += 1
        dias -= 30
        if dias >= 365:
            ano += 1
            dias -= 365

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, meses, dias))