numeros = []

for n in range(1, 101):
    x = int(input())
    numeros.append(x)

maior = max(numeros)
print(maior)
print(numeros.index(maior)+1)