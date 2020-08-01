a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

num = [a, b, c, d, e, f]

lista = []
positivo = 0
for valor in num:
    if valor>0:
        positivo += 1
        lista.append(valor)

print('{} valores positivos'.format(positivo))
print('{}'.format(sum(lista)/positivo))