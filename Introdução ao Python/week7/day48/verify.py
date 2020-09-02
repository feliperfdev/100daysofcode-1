class VerifyMath:

    def __init__(self):
        self.tipo = int
        self.__lista = []

    def __setTypeInt(self, *args):
        VerifyMath.__lista = []
        for num in args:
            VerifyMath.__lista.append(num)
            map(int(x) for x in VerifyMath.__lista)

    def pair(self, *args): # par
        VerifyMath.__setTypeInt(args)
        VerifyMath.__lista = []
        p = list(filter(lambda x: x%2==0, args))
        for num in p:
            VerifyMath.__lista.append(num)
        if len(VerifyMath.__lista) == 1:
            return VerifyMath.__lista[0]
        return [x for x in VerifyMath.__lista]
        
    def odd(self, *args): # ímpar
        VerifyMath.__setTypeInt(args)
        VerifyMath.__lista = []
        p = list(filter(lambda x: x%2!=0, args))
        for num in p:
            VerifyMath.__lista.append(num)
        if len(VerifyMath.__lista) == 1:
            return VerifyMath.__lista[0]
        return [x for x in VerifyMath.__lista]

numero = VerifyMath()

print(numero.pair(*[1, 2, 3, 4]))
print(numero.odd(*[1, 2, 3, 4]))
print(numero.odd(*[1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(numero.pair(19))
print(numero.odd(19))
print(numero.pair(97, 98, 99, 100))
print(numero.odd())