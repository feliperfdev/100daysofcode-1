# ODD -> ímpar
# EVEN -> par
# NULL -> 0
# NEGATIVE / POSITIVE

vezes = int(input())

for n in range(vezes):
    num = int(input())
    if num > 0 and num%2==0:
        print('EVEN POSITIVE')
    if num > 0 and num%2!=0:
        print('ODD POSITIVE')
    if num < 0 and num%2==0:
        print('EVEN NEGATIVE')
    if num < 0 and num%2!=0:
        print('ODD NEGATIVE')
    if num == 0:
        print('NULL')