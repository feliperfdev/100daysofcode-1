'''
Sistema de Arquivos - Navegação

Utilizando o módulo 'os' -> Operational System
'''
print('\n')

import os

# .getcwd() -> retorna o diretório de trabalho atual -> get currently work directory

print(os.getcwd()) # Retorna o Path (caminho) absoluto


# .chdir() -> change directory -> muda de diretório
os.chdir('..') # retorna um diretório para trás
print(os.getcwd())

for diretorio in range(5):
    os.chdir('..')
    print(os.getcwd())

print('\n')
print(os.path.isabs('C:/')) # isabs() --> pergunta se é absoluto

print(os.path.isabs('C:/Users/'))

print(os.name)

import sys

print(sys.platform)