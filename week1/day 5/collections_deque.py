'''
Collections - Deque

-> Podemos dizer que o Deque é uma lista de alta performance
-> Podemos utilizar funções similares às das listas comuns, além de novas funções


'''
print('\n'); from collections import deque

# Criando Deques

deq = deque('felipe')

print(deq) # Ele deu uma espécie de split na string e transformou cada letra como elemento de uma lista

deq.append('r')
print(deq)

deq.appendleft(18) # Adiciona elemento no início da lista
print(deq)

deq.pop()
print(deq)

deq.popleft() # Remove elemento no início da lista
print(deq)