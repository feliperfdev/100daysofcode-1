'''
O que é o método .join() ?

É um método que insere todos os elementos de um iterável separados por aspas

Este método oferece uma forma flexível de criar strings através de um objeto iterável como
listas, strings e tuplas, com elementos separados por aspas. Por fim, retorna uma string concatenada.

Síntaxe: string.joint(iterável)
'''

python = 'Python'
js = 'Javascript'

print(python.join(js)) # fica estranho

csharp = ['C#']
print(python.join(csharp))

# ================================================================================================

teste = ['F', 'e', 'l', 'i', 'p', 'e']
print(''.join(teste)) # Felipe

# ================================================================================================

try:
#       ERRO
    num = [1, 2, 3]
    print(''.join(num))

except Exception:
    #       CORRETO
    num  = list(map(lambda x: str(x), num)) # transformando cada número da lista em string
    # poderia fazer logo -> num = ['1', '2', '3']
    print(''.join(num))