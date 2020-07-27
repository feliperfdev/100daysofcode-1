print('\n')

cidade  = 'Salvador', 'São Paulo', 'Rio de Janeiro'
temperatura = 35, 29, 40

print(list(zip(cidade, temperatura)))

print('\n')

teste = {dado[0]: dado[1] for dado in zip(cidade, temperatura)}
print(teste)

#========================================================================================================
print('\n')


prog = 'Python', 'Java', 'C++', 'Lua', 'Javascript', 'R', 'C#'

rank = 1, 3, 7, 5, 2, 6, 4

organiza = {dado[0]: dado[1] for dado in zip(rank, prog)}

print(organiza); print('\n')

print(sorted(organiza.items(), key=lambda valor: valor))