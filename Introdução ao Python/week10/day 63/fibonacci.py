lista = []

def fibonacci(num: int):
    for i in range(1, num):
        if i==1:
            lista.append(1)
            i += 1
        if i==2:
            lista.append(1)
        else:
            valor = lista[i-1] + lista[i-2]
            lista.append(valor)
    lista[0] = 0
    for elementos in lista:
        print(elementos, end=' ')

def executa():
    valor = int(input('Quantidade de elementos da Sequencia de Fibonacci que deseja: '))
    if (valor > 0 and valor < 46):
        fibonacci(valor)
    else:
        print('Você só pode visualizar até 45 elementos.')

if __name__ == '__main__':
    executa()