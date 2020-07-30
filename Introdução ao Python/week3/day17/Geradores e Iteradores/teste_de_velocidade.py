'''
Teste de Velocidade com Expressões Geradoras


'''
print('\n')

# Generators -> Geradores:

def nums():
    for num in range(1, 11):
        yield num

print(nums()) # <generator object nums at 0x0000011B56DA6C10>

#========================================================================================================

# Generator
gen1 = nums()

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

gen2 = (num for num in nums()) # Generator Expression

print(gen2) # Generation Expression -> <generator object <genexpr> at 0x000001F3FB276970>

print(next(gen2))
print(next(gen2))
print(next(gen2))

print('\n')
#========================================================================================================

print(sum(num for num in range(11)));                               print('\n')

#========================================================================================================

# Fazendo o teste de velocidade

import time

gen_inicio = time.time() # Tempo inicial
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio # Tempo total = tempo de processamento - tempo inicial


list_inicio = time.time()
print(sum([num for num in range(100000000)]));                              print('\n')
list_tempo = time.time() - list_inicio # Tempo total = tempo de processamento - tempo inicial

print(f'O Generator Expression levou {gen_tempo}') # Mais rápido
print(f'O List Comprehension levou {list_tempo}')