'''
Dunder Main & Dunder Name

Dunder Main -> __main__
Dunder Name -> __name__


Em Python, são utilizados Dunder para criar funções, atributos, propriedades.
Utilizamos o Double Under para não gerar conflito com outros nomes no código

=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

Em C temos:

int main(){
    return 0;
}

Em Python, se executarmos diretamente um módulo Python na linha de comando, internamente o
Python atribuirá à variável __name__ o valor __main__, indicando que este é o módulo de
execução principal

'''
print('\n')

print(__name__); print('\n') # ---> __main__

from funcao_parametros import senoIteravel
print(senoIteravel((500, 600, 700)))

import outra_funcao as of

print(of.qualquerFuncao())
