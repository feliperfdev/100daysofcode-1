a, b, c = input().split()
a = float(a); b = float(b); c = float(c)

perimetro = 0
area = 0

if (a < (b+c)) and (b < (a+c)) and (c < (a+b)):
    perimetro = a+b+c
    perimetro = float(perimetro)
    print('Perimetro = {}'.format(perimetro))

else:
    area = ((a+b)*c)/2
    area = float(area)
    print('Area = {}'.format(area))