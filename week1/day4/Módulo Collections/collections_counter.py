'''
Módulo Collections - Counter

Collecions - High-Performance Contarners DataTypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo counter que é parecido com um
dicionário, contendo como chave os elementos da coleção passada e como valor a quantidade de ocorrências
desses elementos

'''

print('\n')

# Utilizando o Counter

from collections import Counter

# Podemos utilizar quaisquer iteráveis

lista = [1, 2, 2, 2, 3, 3, 1, 1, 4, 5, 4, 3, 5, 5, 4, 1, 2, 2, 3, 5]

res = Counter(lista)

print(type(res))
print(res)
# Veja que para cada elemento da lista o Counter criou uma chave e colocou para seus valores a quantidade...
# ... de ocorrências de cada um

#==========================================================================================================
print('\n')

print(Counter('Felipe')) # Transforma cada letra em chave e atribui como valor a quantidade de ocorrências

print('\n')

texto = '''Isso vale até para a evolução das espécies, para a performance das empresas a longo 
prazo e até para nós, dentro desse mundo que muda muito, o tempo todo. E isso acontece principalmente
na nossa área! O nosso computador pode se comparar à história do sistema solar, onde o tempo aqui dentro 
passa tão rápido, que já completou ciclos suficientes para repetir a história do asteróide que cai e 
mata grande parte dos animais, mais de um milhão de vezes. Mas sendo mais específico com a nossa área'''

palavras = texto.split()

res = Counter(palavras)

print(res)

print('\n')
# Encontrando as palavras com mais ocorrências:

print(res.most_common(5)) # As 5 mais comuns

print(res.most_common(10)) # As 10 mais comuns

#==========================================================================================================
