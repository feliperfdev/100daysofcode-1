a, b, c = input().split()
a = int(a); b = int(b); c = float(c)

a2, b2, c2 = input().split()
a2 = int(a2); b2 = int(b2); c2 = float(c2)

# ignorar o 'a' (código do produto) nas contas
# b = quantidade
# c = preço unitário

total = (b*c) + (b2*c2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))