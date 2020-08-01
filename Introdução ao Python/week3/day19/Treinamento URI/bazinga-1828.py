T = int(input())

tesoura = 'tesoura'
papel = 'papel'
pedra = 'pedra'
lagarto = 'lagarto'
Spock = 'Spock'

'''tesoura > papel
papel > pedra
pedra > lagarto
lagarto > Spock
Spock > tesoura
tesoura > lagarto
lagarto > papel
papel > Spock
Spock > pedra
pedra > tesoura'''


for n in range(1, T+1):
    print(n)
    escolha = str(input())

escolha = escolha.split()
print(escolha)

if escolha[0] > escolha[1]:
    assert(escolha[0] > escolha[1])
    print('Caso #{}: Bazinga!'.format(n))
if escolha[0] < escolha[1]:
    print('Caso #{}: Raj trapaceou!'.format(n))
if escolha[0] == escolha[1]:
    print('Caso #{}: De novo!'.format(n))