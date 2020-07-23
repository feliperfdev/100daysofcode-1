'''
Map

-> Com map fazemos mapeamento de valores para função

---> Funcionamento do Map <---

dados iteráveis: a1, a2, a3, ..., an
Temos uma função: f(x)

-> Utilizamos o map() para mapear os elementos dos dados iteráveis e aplicar a função

-> Será retornado: f(a1), f(a2), f(a3), ..., f(an)

'''
print('\n')

import math

def raio(r):
    '''Calcula a área de um círculo com raio "r" '''
    return math.pi * (r**2)

print(raio(4)); print('\n')

#=========================================================================================================

raios = [2, 3, 5, 6]

# Forma comum:

areas = []
for r in raios:
    areas.append(raio(r))

print(areas); print('\n')

# Forma com map:

areas = map(raio, raios) # O map recebe dois argumentos --> 1º: uma função 2º: um iterável qualquer
print(list(areas))                                                      # este iterável será o que...
print(type(areas)); print('\n')                                         # ...sofrerá a função

# Forma utilizando map com lambda:

print(list(map(lambda r: math.pi * (r**2), raios))); print('\n')

'''A variável 'r' é mapeada para cada elemento do iterável 'raios' e será retornada uma expressão
matemática aplicada a este iterável'''

# Calculando fatorial:
valores = [4, 5, 6, 7]

print(list(map(lambda f: math.factorial(f), valores))); print('\n')

#=========================================================================================================

areas = list(map(lambda r: math.pi * (r**2), raios))

[print(x, end=' // ') for x in areas]; print('\n')

# OBS --> Após utilizar o map() pela primeira vez após utilização dos resultados, ele é zerado...
#... ou seja, caso queiramos utilizar novamente, ele deverá ser chamado de novo (oq aconteceu  na l.48)
# --> Fazer teste transformando a l.48 em comentário --> a l.50 não mostrará nenhum resultado
# a variável 'areas' já havia sido declarada anteriormente, não com a mesma sintaxe, mas com o mesmo...
#... objetivo (além de retornar os mesmos valores) --> map(raio, raios)

print(list(map(lambda r: raio(r), valores))); print('\n')

#=========================================================================================================

# ºC para ºF --->       ºF = 9/5 * ºC + 32

cidades = [('Salvador', 30), ('Rio de Janeiro', 35), ('São Paulo', 25), ('Gramado', 15)]
# -->  (Cidade, Temperatura)

print(cidades)
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
#                retorno:  nome(dado[0])+operação(dado[1]=temperatura)  