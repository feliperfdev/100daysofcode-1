'''
Geradores (Generators)

--> Geradores são Iteradores (Iterators), mas Iteradores não são Geradores.

-> Geradores podem ser criados com funções geradoras
-> Funções geradoras utilizam a palavra reservada yield
-> Generators podem ser criados com expressões geradoras

'''
print('\n')

# Diferença entre Funções e Generator Function

#===========================================================================================
#              Funções                       |         Generator Functions                 |
#===========================================================================================
#    Utilizam return                         |        Utilizam yield                       |
#===========================================================================================
#    retorna uma vez                         |        podem utilizar yield várias vezes    |
#===========================================================================================
#    quando executada, retorna um valor      |     quando executada, retorna um generator  |
#===========================================================================================

# Função Geradora:

def conta_ate(num_max):
    cont = 1
    while cont <= num_max:
        yield cont
        cont += 1

# Uma generator function NÃO é um generator. Ela GERA um generator.

gen = conta_ate(5)
print(type(gen)) # generator

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen));                                                   print('\n')
#print(next(gen)) --> Erro StopIteration --> Passou da quantidade de acordo com o valor fornecido

print([x for x in conta_ate(33)]);                  print('\n')

#======================================================================================================

gen_num = conta_ate(7)

print(next(gen_num)) # 1
print('Python')

for x in gen_num:
    print(x)    # começa a partir do 2

#======================================================================================================
print('\n')

gen_todos = list(conta_ate(8))
print(gen_todos)