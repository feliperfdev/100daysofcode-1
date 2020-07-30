'''
Teste de Memória com Geradores


Sequência de Fibonacci: 1, 1, 2, 3, 5, 8, 13...
'''
print('\n')

# Função usando lista

def fibonacci(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a, b = b, a+b
    return num


print(fibonacci(10))

print([x for x in fibonacci(10)])

from sys import getsizeof

print(getsizeof(fibonacci(100000))) # 824456 bytes
print(getsizeof([x for x in fibonacci(100000)])) # 824456 bytes

print('\n')
# Função usando geradores

def fibonacci_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b = b, a+b
        yield a
        cont += 1

print(fibonacci_gen(10)) # <generator object fibonacci_gen at 0x000001C162B86970>

print(x for x in fibonacci_gen(10)) #<generator object <genexpr> at 0x000001FC95C96B30>

print(list(fibonacci_gen(10)));                          print('\n')

print(getsizeof(fibonacci_gen(100000))) # 112 bytes
print(getsizeof(list(fibonacci_gen(100000)))) # 879832 bytes

print('\n')
# Iterando no gerador:

for x in fibonacci_gen(10):
    print(x, end=' ')