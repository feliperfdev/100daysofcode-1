from math import sin

def senoIteravel(lista):
    pega = (sin(num) for num in lista)
    return list(pega)

if __name__ == "__main__":
    lista1 = [100, 200, 300, 400]
    print(lista1)

    tupla1 = 900, 800, 700, 600
    print(tupla1)
else:
    print('O módulo foi importado!')