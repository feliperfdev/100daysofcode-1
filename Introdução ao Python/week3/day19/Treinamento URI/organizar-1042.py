a, b, c = input().split()
lista = []
a, b, c = int(a), int(b), int(c)
lista.append(a)
lista.append(b)
lista.append(c)

lista = sorted(lista)

for num in lista:
    print(num)

print()
lista = a, b, c
for num in lista:
    print(num)