m = None
n = None
while m!=0 or n!=0:

    m, n = input().split()
    m = int(m); n = int(n)

    soma = 0

    if n <= 0 or m <= 0:
        break

    if m < n:
        for value in range(m, n+1):
            soma += value
            print(value, end=' ') 
        print('Sum={}'.format(soma))

    elif n < m:
        n, m = m, n
        for value in range(m, n+1):
            soma += value
            print(value, end=' ')
        print('Sum={}'.format(soma))