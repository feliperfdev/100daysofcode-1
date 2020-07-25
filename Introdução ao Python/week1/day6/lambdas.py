'''
Funções Lambda

-> São funções sem nome. Assim como as funções python, recebem parâmetros e retornam valores.

'''
print('\n')

calc = lambda x: (3*x) + 1
print(calc(12))

#=========================================================================================================
print('\n')

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('felipe', 'ribeiro'))

# .strip() --> remove espaços vazios que separam as palavras das aspas
# para remover espaços vazios que separam letras (e qualquer outra coisa), usar:
# ---> str.replace(' ', '')   -----> entenda 'str' como qualquer string ou variável de string

print(nome_completo('FELIPE         ', 'ribeiro'))
print(nome_completo('       felipe', '   RIBEIRO     '))

#=========================================================================================================
print('\n')

uma = lambda x: 3*x*x*7
duas = lambda x, y: 1 + (1/x + 1/y)**0.5
tres = lambda x, y, z: 1 + float(1/x + 1/y + 1/z) + (x*y*z)

print(uma(3))
print(duas(12, 4))
print(tres(3, 4, 7))

#=========================================================================================================
print('\n')

autores = ['Robert Bryndza', 'Sarah J. Maas', 'Paula Hawkings', 'Stephen King']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# O que aconteceu?
# --> Relembrando: .sort() -> faz ordenação
# foi passado como argumento um lambda que recebe uma variável (chamada de sobrenome)
# essa variável recebe o método .spli(' ') --> que separa em uma lista tudo que estiver separado...
# por um espaço vazio --> por isso o parâmetro (' ')
# depois já é pedido para acessar o último elemento dessa lista ---> [-1]

# o método .lower() foi chamado apenas para colocar em caixa baixa esses elementos que foram acessados...
#... mas pq esse método foi aplicado? Apenas para validação. Para que não ocorresse que sobrenomes com...
#... a primeira letra em caixa alta não sobrepusessem os sobrenomes com a primeira letra em caixa baixa...
#... mas, com toda certeza esse método .lower() poderia ser removido sem causar qualquer alteração...
#... caso não consideremos tal exceção. Basta escrever os nomes corretamente
# --> autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1]) --> mesmo resultado

#=========================================================================================================
print('\n')

# Exemplo --> Função Quadrática:

# ---> f(x)=a*x**2 + b*x + c

def geraFuncaoQuadratica(a, b, c):
    "Gera uma função do tipo ax²+bx+c"
    return lambda x: a*x**2 + b*x + c

quadratica = geraFuncaoQuadratica(3, 7, 8) # Atribuindo valores às variáveis a, b e c e guardando numa...
#... variável que vai exercer a função lambda, podendo receber um valor como argumento

print(quadratica(5))

# ou podemos fazer:

print(geraFuncaoQuadratica(3, 4, -5)(8)) # --> o segundo parêntese corresponde ao valor de 'x'