ddd = int(input())

dedede = [61, 71, 11, 21, 32, 19, 27, 31]
cidade = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 
'Campinas', 'Vitoria', 'Belo Horizonte']

if ddd in dedede:
    print(cidade[dedede.index(ddd)])
else:
    print('DDD nao cadastrado')