def myRange(start: int, final: int, step=1):
    cont = start
    while cont <= final-1:
        print(cont, end=' ')
        cont += step

def myRangeList(start: int, final: int, step=1) -> list:
    array = []
    cont = start
    while cont <= final-1:
        array.append(cont)
        cont += step
    print(array)

def rangeSoma(start: int, final: int, step=1) -> int:
    soma = 0
    for i in range(start, final, step):
        soma += i
    print(soma)

myRange(1, 10, 3); print()
myRangeList(34, 57, 2); print()
rangeSoma(1, 30, 2)