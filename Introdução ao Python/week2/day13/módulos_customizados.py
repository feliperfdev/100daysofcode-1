'''
Módulos Customizados

Como módulos python nada mais são que arquivos python, então todos os arquivos que foram criados no desafio,
são módulos python prontos para serem utilizados
'''
print('\n')

from quadratica import geraFuncaoQuadratica

valor_x = geraFuncaoQuadratica(3, 4, 7)

print(valor_x(10))

from funcao_parametros import senoIteravel

print(senoIteravel([30, 60, 90, 120])); print('\n')

tupla = -30, -45, -60

print(senoIteravel(tupla))
