from time import sleep

print('--------------------Lista--------------------')
nome_lista = input('Digite o nome da lista: ')
print(f'--------------------{nome_lista}--------------------')

with open(f'{nome_lista}.txt', 'w') as arquivo:
    arquivo.write(f'--------------------{nome_lista}--------------------\n\n')
    escolha = () 

    try:
        while(escolha != 2):
            print('O que deseja fazer? ')
            escolha = int(input('\n[1] - Adicionar elemento na lista\n[2] - Sair da lista\n'))
            if (escolha == 1):
                elemento = int(input('Quantidade de elementos: '))
                for e in range(1, elemento+1):
                    elemento = input('')
                    arquivo.write(f'{elemento}\n')
            if (escolha == 2):
                    arquivo.close()
    except Exception as error:
        print(f'\nOpa! Aparentemente, ocorreu um erro. {error.__class__}')
    finally:
        print('\nObrigado por usar a lista.')
    sleep(1.5)