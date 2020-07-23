def hello_world():
    """"Função que retorna o texto 'Hello, World!'""""" #Documentação -> docstring
    return 'Hello, World!'

print(hello_world()) #Passar o mouse por cima da função para ver o texto documentado

print(hello_world.__doc__) #imprimindo a documentação de uma função

print("\n")
print('LEN: ' + len.__doc__); print("\n")
print('ENUMERATE: ' + enumerate.__doc__); print("\n")
print('RANGE: ' + range.__doc__)


def exponencial(base, potencia=2):
    """""
    Função que retorna, por padrão, o quadrado de um número.
    
    potencia = 2 -> padrão (caso nada seja informado)
    potencia = ... -> o número informado é validado como potencia
    base = argumento obrigatório
    
    base ** potencia
    """""
    return base ** potencia

print(exponencial.__doc__)
print(exponencial(6))
print(exponencial(5, 7))