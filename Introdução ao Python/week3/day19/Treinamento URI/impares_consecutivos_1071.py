x = int(input())
y = int(input())

soma = 0
if x >= y:
    for valor in range(x-1, y, -1):
        if valor%2!=0:
            soma += valor
    print(soma)

elif y >= x:
    x, y = y, x
    for valor in range(x-1, y, -1):
        if valor%2!=0:
            soma += valor
    print(soma)