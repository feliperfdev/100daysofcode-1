lista = [1, 2, 3, 4, 5]

def listSum(*args):
    def soma():
        s = 0
        for e in args:
            s += e
            return s
    return soma

print(listSum(*lista))

#=============================================================================

def elevaAoQuadrado(x):
    return x**2
resp = list(map(elevaAoQuadrado, [1, 2, 3, 4, 5]))

print(resp)

#=============================================================================

nomes = ['Felipe', 'Clara', 'Adriano', 'Eduardo', 'Amanda']

nomes = sorted(nomes, key=len)
print(nomes)

testeFilter = list(filter(lambda x: len(x) <= 5, nomes))

print(testeFilter)

#=============================================================================

binario = [1, 1, 1, 0]  # 1-> true 0 -> false

testeAny = any(binario)
print(testeAny) # True

testeAll = all(binario)
print(testeAll) # False

'''
Olhar week2 day 8 para entender any() e all()
'''
#=============================================================================
