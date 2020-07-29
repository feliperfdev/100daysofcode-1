'''
Criando a própria versão de Loop


'''
print('\n')

for num in [1, 2, 3, 4, 5]:
    print(num, end=' ')

print('\n')
for letra in 'Python':
    print(letra, end=' ')

#=========================================================================================================

print('\n')
def novo_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            break

novo_for([1, 2, 3, 4, 5])