casos = int(input())

for i in range(1, casos+1):

    string = str(input()).lower()
    string = string.split()
    string.sort()
    for palavra in string:
        print(palavra, end=' ')
    print()